
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [

    url(r'^excalibur/', include('forms.urls')),
    url(r'^movies/', include('forms.urls')),
    url(r'^series/', include('series.urls')),
    url(r'^admin/', admin.site.urls),
]
