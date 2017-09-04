from django.contrib import admin

# Register your models here.
from forms.models import Genres,Movies,Actors

admin.site.register(Genres)
admin.site.register(Actors)

admin.site.register(Movies)
