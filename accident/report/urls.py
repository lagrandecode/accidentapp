from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
import os


urlpatterns = [

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
