"""URL endpoints for Vault api app
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from vault.views import SecretItemView, SecretNotesView, SecretLoginView

ROUTER = DefaultRouter()
ROUTER.register(r"items", SecretItemView)
ROUTER.register(r"notes", SecretNotesView)
ROUTER.register(r"logins", SecretLoginView)

urlpatterns = [path("", include(ROUTER.urls))]
