from django.views.generic import FormView, DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from series.models import Series, Episode


# Create your views here.
class SeriesView(ListView):
    template_name = "pages/series.html"
    model = Series

def series_detail(request, pk):
    episode_list = get_object_or_404(Episode, pk=article.id)
    return render('pages/series_detail.html', episode_list)    