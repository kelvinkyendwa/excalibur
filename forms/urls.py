from django.conf.urls import url

# from forms.views import IndexView
from forms.views import MoviesView, IndexView, Movie_detail
from forms import views
from django.shortcuts import render

app_name = 'forms'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^movies/', MoviesView.as_view(), name= 'movies'),
    url(r'^review/(?P<pk>\d+)/$', Movie_detail.as_view(), name= 'movie_detail'),
    # url(r'^series/', SeriesView.as_view(), name='series'),
    # url(r'^episode/(?P<pk>\d+)/$', Series_detail.as_view(), name= 'series_detail'),

]
