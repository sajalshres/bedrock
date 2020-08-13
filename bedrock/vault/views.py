"""Views for Vault api app
"""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from vault.models import SecretItem, SecretLogin, SecretNotes
from vault.serializers import (
    SecretItemSerializer,
    SecretNotesSerializer,
    SecretLoginSerializer,
)


class VaultAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class_item = SecretItemSerializer
    serializer_class_login = SecretLoginSerializer
    serializer_class_note = SecretNotesSerializer

    def get_queryset_item(self):
        return SecretItem.objects.all()

    def get_queryset_login(self):
        return SecretLogin.objects.all()

    def get_queryset_note(self):
        return SecretNotes.objects.all()

    def list(self, request, *args, **kwargs):
        item = self.serializer_class_item(
            data=self.get_queryset_item(), many=True
        )
        item.is_valid()

        login = self.serializer_class_login(
            data=self.get_queryset_login(), many=True
        )
        login.is_valid()

        note = self.serializer_class_note(
            data=self.get_queryset_note(), many=True
        )
        note.is_valid()

        return Response(
            [*item.data, *login.data, *note.data], status=status.HTTP_200_OK
        )


class SecretItemView(viewsets.ModelViewSet):
    """Rest view for secret items
    """

    queryset = SecretItem.objects.all()
    serializer_class = SecretItemSerializer
    permission_classes = [IsAuthenticated]


class SecretLoginView(viewsets.ModelViewSet):
    """Rest view for secret items
    """

    queryset = SecretLogin.objects.all()
    serializer_class = SecretLoginSerializer
    permission_classes = [IsAuthenticated]


class SecretNotesView(viewsets.ModelViewSet):
    """Rest view for secret notes
    """

    queryset = SecretNotes.objects.all()
    serializer_class = SecretNotesSerializer
    permission_classes = [IsAuthenticated]
