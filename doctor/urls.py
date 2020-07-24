from django.contrib import admin
from django.urls import path
from .views import doctor

urlpatterns = [
    path('',doctor,name='doctor'),
]

