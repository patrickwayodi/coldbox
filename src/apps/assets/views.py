"""
https://learndjango.com/tutorials/django-file-and-image-uploads-tutorial
"""


import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, View

from .forms import AssetForm
from .models import Asset, Asset


# Get an instance of a logger
logger = logging.getLogger(__name__)


class HomeView(ListView):
    
    model = Asset
    
    template_name = "assets/home.html"

    def get_queryset(self, **kwargs):

        # queryset = Asset.objects.all()[:5]
        
        queryset = Asset.objects.order_by("-id")[:5]

        return queryset

    def get_context_data(self, **kwargs):

        context = super(HomeView, self).get_context_data(**kwargs)

        context['assets'] = Asset.objects.order_by("-id")[:5]

        return context


class CreateAssetView(CreateView):

    model = Asset

    form_class = AssetForm

    template_name = "assets/upload.html"

    success_url = reverse_lazy("home")


class AssetDetailView(DetailView):

    template_name = "assets/asset_detail.html"

    model = Asset

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["asset"] = get_object_or_404(Asset, pk=self.kwargs["pk"])
        
        return context
