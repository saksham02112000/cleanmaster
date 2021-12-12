from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('data/', handler),
    path('picked', picked),
    path('path', trav),
    path('masterreset', masterreset),
    path('status', dustbin_status),
    path('status_demo', demo_ml),
    path('handler', handler)

]
