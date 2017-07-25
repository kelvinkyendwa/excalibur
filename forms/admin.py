from django.contrib import admin

# Register your models here.
from forms.models import Genres,Movies,Series,Actors,Episode

admin.site.register(Genres)
admin.site.register(Actors)
admin.site.register(Series)
admin.site.register(Movies)
admin.site.register(Episode)
