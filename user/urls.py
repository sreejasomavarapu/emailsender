from django.contrib import admin
from django.urls import path
from . views import *
urlpatterns = [
    path('contact/', contact, name ='contact'),
    path('contactnext/', contactnext, name ='contactnext'),
    path('plans/', plans, name ='plans'),
    path('planbook/', planbook, name ='planbook'),
]


