from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView, DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from series.models import Series,Episode,Genres
from django.utils import timezone


# Create your views here.
class SeriesView(ListView):
    template_name = "pages/series.html"
    model = Series
    def get_context_data(self, **kwargs):
        context = super(SeriesView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class Series_detail(DetailView):
    model = Episode

    template_name = "pages/series_detail.html"
    def get_context_data(self, **kwargs):
        context = super(Series_detail, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
