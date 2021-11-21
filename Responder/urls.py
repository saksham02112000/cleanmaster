from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('data/', handler),
    path('picked', picked),
    path('path', trav),
    path('masterreset', masterreset)

]
