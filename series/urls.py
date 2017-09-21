from django.conf.urls import url

# from forms.views import IndexView
from series.views import SeriesView, Series_detail
from forms.views import IndexView
from series import views
from django.shortcuts import render

app_name = 'series'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^series/', SeriesView.as_view(), name='series'),
    url(r'^series/(?P<pk>\d+)/episodes/$', Series_detail.as_view(), name='series_detail'),

]
