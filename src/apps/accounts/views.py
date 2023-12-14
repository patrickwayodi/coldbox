from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import AccountCreationForm


class HomeView(TemplateView):
    
    template_name = "accounts/accounts_home.html"


class SignUpView(CreateView):

    form_class = AccountCreationForm

    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'
