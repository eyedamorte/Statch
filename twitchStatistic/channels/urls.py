from django.contrib import admin
from django.urls import path, include

from channels.views import *

app_name = 'channels'

urlpatterns = [
   path('list/', channels_list_get)
]