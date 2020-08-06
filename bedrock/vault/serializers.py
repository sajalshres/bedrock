"""Serializers for Vault api app models
"""
from rest_framework import serializers
from rest_framework.utils import model_meta
from rest_framework.exceptions import ValidationError

from sor.serializers import ManyToManyRelatedField
from sor.models import Label
from vault.models import SecretItem, SecretLogin, SecretNotes, Link


class SecretItemSerializer(serializers.ModelSerializer):
    """SecretItem model serializer
    """

    labels = ManyToManyRelatedField()

    class Meta:
        model = SecretItem
        fields = ["id", "title", "name", "value", "note", "labels", "type"]

    def create(self, validated_data):
        ModelClass = self.Meta.model
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}

        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        instance = ModelClass._default_manager.create(**validated_data)

        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

    def update(self, instance, validated_data):
        model_field_info = model_meta.get_field_info(instance)

        many_to_many_fields = []

        for attr, value in validated_data.items():
            if (
                attr in model_field_info.relations
                and model_field_info.relations[attr].to_many
            ):
                many_to_many_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        for attr, value in many_to_many_fields:
            field = getattr(instance, attr)
            field.set(value)

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


class SecretLoginSerializer(serializers.ModelSerializer):
    """SecretLogin model serializer
    """

    pass


class SecretNotesSerializer(serializers.ModelSerializer):
    """SecretNotes model serializer
    """

    pass
