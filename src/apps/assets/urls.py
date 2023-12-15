from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import CreateAssetView, AssetDetailView, HomeView


urlpatterns = [

    path("assets/", HomeView.as_view(), name='assets_home'),
    # path("upload/", CreateAssetView.as_view(), name="create_asset"),
    path("asset/new/", CreateAssetView.as_view(), name="create_asset"),
    path("asset/<int:pk>/", AssetDetailView.as_view(), name='asset_detail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
