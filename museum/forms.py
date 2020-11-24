from django import forms
from .models import Review, Application, Event
from django.forms import ModelForm, DateInput


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats parses HTML5 datetime-local input to datetime field
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class AddReviewForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        review = Review(**self.clean())
        review.save()
        return review


class AddApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    email = forms.EmailField()
    count_users = forms.IntegerField()
    date_application = forms.DateField()

    def clean(self):
        return self.cleaned_data

    def save(self):
        application = Application(**self.clean())
        application.save()
        return application
