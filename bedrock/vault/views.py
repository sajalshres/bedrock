"""Views for Vault api app
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from vault.models import SecretItem, SecretLogin, SecretNotes, Link
from vault.serializers import SecretItemSerializer


class SecretItemView(viewsets.ModelViewSet):
    """Rest view for secret items
    """

    queryset = SecretItem.objects.all()
    serializer_class = SecretItemSerializer
    permission_classes = [IsAuthenticated]

