from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include('apps.accounts.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include('apps.assets.urls')),
    path("", include('apps.gatepasses.urls')),
]
