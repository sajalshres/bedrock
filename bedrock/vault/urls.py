"""URL endpoints for Vault api app
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from vault.views import SecretItemView

ROUTER = DefaultRouter()
ROUTER.register(r"items", SecretItemView)

urlpatterns = [path("", include(ROUTER.urls))]
