

# Register your models here.
from django.contrib import admin

# Register your models here.
from series.models import Genres,Actors,Series,Episode

admin.site.register(Genres)
admin.site.register(Series)
admin.site.register(Actors)
admin.site.register(Episode)
