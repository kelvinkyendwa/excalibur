from django.views.generic import TemplateView
from django.views.generic import FormView
from django.shortcuts import render
from django.core.mail import send_mail
from . import forms

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

class IndexView(TemplateView):
    template_name = "forms/index.html"
class MoviesView(TemplateView):
    template_name = "pages/movies.html"
def feedback(request):
    form = forms.FeedbackForm()

    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)

        if form.is_valid():

            print("validation Success")
            print("Name:" +form.cleaned_data['name'])
            print("Email:" +form.cleaned_data['email'])
            print("Information left:" +form.cleaned_data['text'])
    return render(request,'forms/feedback.html',{'form':form})