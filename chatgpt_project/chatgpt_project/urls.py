from django.contrib import admin
from django.urls import path, include

from .views import google_login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat.urls")),
    path('accounts/', include('allauth.urls')),
]
