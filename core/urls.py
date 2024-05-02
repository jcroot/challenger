from django.contrib import admin
from django.urls import path

from core import api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += api_urls.urlpatterns
