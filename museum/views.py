from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta, date
from .forms import AddReviewForm, AddApplicationForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.views import generic
from django.utils.safestring import mark_safe
import calendar
from .models import *
from .utils import Calendar


def about(request):
    return render(request, 'museum/about.html')


def afisha(request):
    return render(request, 'museum/afisha.html')


def paginationPage(request, item, url):
    page = request.GET.get('page', 1)
    limit = 2
    paginator = Paginator(item, limit)
    paginator.baseurl = url + '?page='
    page = paginator.page(page)
    pl = [page, paginator]
    return pl


def paginationPageBook(request, item, url):
    page = request.GET.get('page', 1)
    limit = 1
    paginator = Paginator(item, limit)
    paginator.baseurl = url + '?page='
    page = paginator.page(page)
    pl = [page, paginator]
    return pl


def paginationPageReview(request, item, url):
    page = request.GET.get('page', 1)
    limit = 4
    paginator = Paginator(item, limit)
    paginator.baseurl = url + '?page='
    page = paginator.page(page)
    pl = [page, paginator]
    return pl


def news(request):
    new = New.objects.NewsSortByDate()
    image = NewImage.objects.all()
    pl = paginationPage(request, new, '/news/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/news.html',
                  {
                      'news': page.object_list,
                      'image': image,
                      'paginator': paginator,
                      'page': page
                  })


def guests(request):
    guest = Guest.objects.all().order_by('-dateReview')
    pl = paginationPageBook(request, guest, '/guests/')
    page, paginator = pl[0], pl[1]
    return render(request, 'museum/museum-category/book/bookHonoraryGuest.html',
                  {
                      'guest': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


def reviews(request):
    reviews = Review.objects.all().order_by('-date_review')
    pl = paginationPageReview(request, reviews, '/reviews/')
    page, paginator = pl[0], pl[1]
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reviews/')
    else:
        form = AddReviewForm()
    return render(request, 'museum/reviews.html', {'form': form,
                                                   'reviews': page.object_list,
                                                   'paginator': paginator,
                                                   'page': page})


def exursion(request):
    excursions = New.objects.ExcursionsCategory()
    pl = paginationPage(request, excursions, '/exursion/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/museum-category/Exursiion.html',
                  {
                      'excursions': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


def graduates(request):
    graduates = New.objects.GraduatesCategory()
    pl = paginationPage(request, graduates, '/graduates/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/museum-category/Graduets.html',
                  {
                      'graduates': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


def maecenases(request):
    maecenases = New.objects.MaecenasesCategory()
    pl = paginationPage(request, maecenases, '/maecenases/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/museum-category/Graduets.html',
                  {
                      'maecenases': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


def veterans(request):
    veterans = New.objects.VeteransCategory()
    pl = paginationPage(request, veterans, '/veterans/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/museum-category/Veterans.html',
                  {
                      'veterans': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


def museumNal(request):
    museumNal = New.objects.MuseumNal()
    pl = paginationPage(request, museumNal, '/museumNal/')
    page, paginator = pl[0], pl[1]

    return render(request, 'museum/museum-category/MuseumNalkovskoi.html',
                  {
                      'museumNal': page.object_list,
                      'paginator': paginator,
                      'page': page
                  })


class CalendarView(generic.ListView):
    model = Event
    template_name = 'museum/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        graduates = New.objects.Graduates()
        excursions = New.objects.Excursions()
        maecenases = New.objects.Maecenases()
        veterans = New.objects.Veterans()
        image = NewImage.objects.all()
        count = [0, 1, 2, 3]
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['excursions'] = excursions
        context['maecenases'] = maecenases
        context['graduates'] = graduates
        context['veterans'] = veterans
        context['image'] = image
        context['count'] = count
        return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('main'))
    return render(request, 'museum/museum-category/event.html', {'form': form})
