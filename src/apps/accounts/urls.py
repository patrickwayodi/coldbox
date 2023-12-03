from django.shortcuts import render
from django.urls import path
from django.views.generic.base import TemplateView

from .views import SignUpView

urlpatterns = [

    path("signup/", SignUpView.as_view(), name="signup"),
    path("", TemplateView.as_view(template_name="accounts/home.html"), name="home"),

]
