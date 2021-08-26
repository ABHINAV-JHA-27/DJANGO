from django.contrib import admin
from django.urls import path
from HOME import views

urlpatterns = [
    path("",views.index, name='HOME'),
    path("gallery",views.gallery, name='GALLERY'),
    path("aboutme",views.aboutme, name='ABOUT_ME'),
    path("contact",views.contact, name='CONTACT_ME')
]