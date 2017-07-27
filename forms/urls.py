from django.conf.urls import url

# from forms.views import IndexView
from forms.views import MoviesView,SeriesView
from forms import views
from django.shortcuts import render

urlpatterns = [
    url(r'^register/', views.register,name = 'register'),
    url(r'^review/', views.review_movie,name = 'review'),
    url(r'^$', views.index, name='index'),
    url(r'^feedback/',views.feedback, name='feedback'),
    url(r'^movies/',MoviesView.as_view()),
    url(r'^series/', SeriesView.as_view(), name='series'),
]
