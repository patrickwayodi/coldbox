from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic.base import TemplateView


from .views import CreateGatepassView, GatepassDetailView, HomeView


urlpatterns = [

    path("gatepasses/", HomeView.as_view(), name='gatepasses_home'),
    path("gatepass/upload/", CreateGatepassView.as_view(), name="upload_gatepass_collection"),
    path("gatepass/<int:pk>", GatepassDetailView.as_view(), name='gatepass_detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
