from django.shortcuts import render
from django.urls import path
from django.views.generic.base import TemplateView

from .views import HomeView, SignUpView


urlpatterns = [

    # path("", TemplateView.as_view(template_name="accounts/home.html"), name="home"),
    path("", HomeView.as_view(), name="accounts_home"),
    path("signup/", SignUpView.as_view(), name="signup"),

]
