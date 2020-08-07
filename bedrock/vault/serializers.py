"""Serializers for Vault api app models
"""
from rest_framework import serializers
from rest_framework.utils import model_meta
from rest_framework.exceptions import ValidationError

from common.fields import ManyToManyRelatedField
from common.mixins import NestedSerializerMixin
from sor.models import Label
from vault.models import SecretItem, SecretLogin, SecretNotes, Link


class SecretItemSerializer(serializers.ModelSerializer, NestedSerializerMixin):
    """SecretItem model serializer
    """

    labels = ManyToManyRelatedField()

    class Meta:
        model = SecretItem
        fields = ["id", "title", "name", "value", "note", "labels", "type"]

    def validate_labels(self, value):
        labels = []

        for label_name in value:
            try:
                labels.append(Label.objects.get(name=label_name))
            except Label.DoesNotExist:
                msg = "Label %s matching query does not exist" % label_name
                raise ValidationError([msg])
        return labels


class SecretLoginSerializer(serializers.ModelSerializer):
    """SecretLogin model serializer
    """

    pass


class SecretNotesSerializer(
    serializers.ModelSerializer, NestedSerializerMixin
):
    """SecretNotes model serializer
    """

    labels = ManyToManyRelatedField()

    class Meta:
        model = SecretNotes
        fields = ["id", "title", "note", "labels", "type"]

    def validate_labels(self, value):
        labels = []

        for label_name in value:
            try:
                labels.append(Label.objects.get(name=label_name))
            except Label.DoesNotExist:
                msg = "Label %s matching query does not exist" % label_name
                raise ValidationError([msg])
        return labels
