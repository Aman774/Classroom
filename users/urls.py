
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('login/', views.LoginFun.as_view(),name="login"),
     path('registration/', views.Registation.as_view(), name="registration"),

    
]
