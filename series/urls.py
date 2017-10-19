from django.conf.urls import url
from series.views import SeriesView
from forms.views import IndexView
from . import views

app_name = 'series'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^series/', SeriesView.as_view(), name='series'),
    url(r'^series/(?P<pk>\d+)/', views.series_detail, name='series_detail'),

]
