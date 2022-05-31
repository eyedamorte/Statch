from django.contrib import admin
from django.urls import path, include

from streamers.views import *

app_name = 'streamers'

urlpatterns = [
   path('list/', streamers_list_get)
]