"""Serializers for Vault api app models
"""
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from common.fields import ManyToManyRelatedField
from common.mixins import NestedSerializerMixin
from sor.models import Label
from vault.fields import URLListField
from vault.models import SecretItem, SecretLogin, SecretNotes


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


class SecretLoginSerializer(
    serializers.ModelSerializer, NestedSerializerMixin
):
    """SecretLogin model serializer
    """

    labels = ManyToManyRelatedField()
    links = URLListField()

    class Meta:
        model = SecretLogin
        fields = [
            "id",
            "title",
            "username",
            "password",
            "links",
            "note",
            "labels",
            "type",
        ]

    def create(self, validated_data):
        links = validated_data.pop("links", [])
        instance = super().create(validated_data)

        for link in links:
            instance.links.create(url=link)

        return instance

    def update(self, instance, validated_data):
        links = validated_data.pop("links", [])
        instance = super().update(instance, validated_data)

        instance.links.all().delete()

        for link in links:
            instance.links.update_or_create(url=link)

        return instance

    def validate_labels(self, value):
        labels = []

        for label_name in value:
            try:
                labels.append(Label.objects.get(name=label_name))
            except Label.DoesNotExist:
                msg = "Label %s matching query does not exist" % label_name
                raise ValidationError([msg])
        return labels


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
