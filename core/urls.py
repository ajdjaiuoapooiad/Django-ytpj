from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('',views.homepage),
    path('contact/',views.contact),
    path('about/',views.aboutpage),
]