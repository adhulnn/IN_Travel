from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns=[
    path('',runstatic,name="index"),
    path('register/',register,name="register"),
    path('login/',login,name='login'),
    path('logout/',user_logout,name='logout'),
]