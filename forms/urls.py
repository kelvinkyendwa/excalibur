from django.conf.urls import url

# from forms.views import IndexView
from forms.views import MoviesView, SeriesView, IndexView, Movie_detail
from forms import views
from django.shortcuts import render


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^movies/', MoviesView.as_view(), name= 'movies'),
    url(r'^review/(?P<pk>\d+)/$', Movie_detail.as_view(), name= 'movie_detail'),
    url(r'^series/', SeriesView.as_view(), name='series'),
]
