from django.contrib import admin

from .models import New, NewImage, Review, Event, Guest


class NewImageInline(admin.TabularInline):
    model = NewImage


class NewAdmin(admin.ModelAdmin):
    inlines = [
        NewImageInline,
    ]
    list_display = ('title', 'date', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_review')


admin.site.register(New, NewAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Event)
admin.site.register(Guest)