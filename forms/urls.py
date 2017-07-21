from django.conf.urls import url

from forms.views import IndexView
from forms.views import MoviesView
from forms import views
from django.shortcuts import render

urlpatterns = [
    url(r'^register/', views.register,name = 'register'),
    url(r'^$', IndexView.as_view()),
    url(r'^feedback/',views.feedback, name='feedback'),
    url(r'^movies/',MoviesView.as_view()),
]
