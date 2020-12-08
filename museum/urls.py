from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='main'),
    path('afisha/', views.afisha, name='afisha'),
    path('about/', views.about, name='about us'),
    path('news/', views.news, name='news'),
    path('reviews/', views.reviews, name='reviews'),
    path('exursion/', views.exursion, name='exursion'),
    path('graduates/', views.graduates, name='graduates'),
    path('maecenases/', views.maecenases, name='maecenases'),
    path('veterans/', views.veterans, name='veterans'),
    path('museumNal/', views.museumNal, name='museumNal'),
    path('event/new/', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('guests/', views.guests, name='guests'),

]
