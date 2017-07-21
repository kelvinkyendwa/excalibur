from django import forms
from django.core import validators


class FeedbackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    ver_email = forms.EmailField(label='Enter email agquain')
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        veri_email = all_clean_data['ver_email']

        if email != veri_email:
            raise forms.ValidationError("Can you Can you can you match")




class RegisterForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
