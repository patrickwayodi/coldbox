"""
https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial
TODO: Implement logging to a file (gatepasses.log).
"""


import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View

from .forms import GatepassForm
from .models import Gatepass


# Get an instance of a logger
logger = logging.getLogger(__name__)


class HomeView(ListView):
    
    model = Gatepass
    
    template_name = "gatepasses/home.html"

    def get_queryset(self, **kwargs):

        # queryset = Gatepass.objects.all()[:5]
        
        queryset = Gatepass.objects.order_by("-id")[:5]

        return queryset

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)

        context['gatepasses'] = Gatepass.objects.order_by("-id")[:5]

        return context


class CreateGatepassView(CreateView):

    model = Gatepass

    form_class = GatepassForm

    template_name = "gatepasses/create_gatepass.html"

    success_url = reverse_lazy("gatepasses_home")


class GatepassDetailView(DetailView):

    template_name = "gatepasses/gatepass_detail.html"

    model = Gatepass

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["gatepass"] = get_object_or_404(Gatepass, pk=self.kwargs["pk"])
        
        return context
