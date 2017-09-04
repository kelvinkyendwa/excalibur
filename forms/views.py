from django.views.generic import TemplateView
from django.views.generic import FormView, DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from forms.models import Movies,Genres,Actors
from . import forms
from forms.forms import AddActors
from django.utils import timezone


def register(request):
    reg_form = forms.RegisterForm()

    if request.method == 'POST':
        reg_form = forms.RegisterForm(request.POST)

        if form.is_valid():

            print("validation Success")
            print("Name:" +reg_form.cleaned_data['name'])
            print("Email:" +reg_form.cleaned_data['email'])
            print("Information left:" +reg_form.cleaned_data['text'])
    return render(request,'forms/register_form.html',{'regisrty':reg_form})

# def index(request):
#     return render(request,'forms/index.html')
class IndexView(TemplateView):
    template_name = "forms/index.html"
class MoviesView(ListView):

    template_name = "pages/movies.html"
    model = Movies
class Movie_detail(DetailView):
    model = Movies

    template_name = "pages/movie_detail.html"
