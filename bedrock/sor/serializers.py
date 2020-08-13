"""Serializers for SOR api app models
"""
from rest_framework import serializers
from rest_framework.utils import model_meta
from rest_framework.exceptions import ValidationError

from common.fields import ManyToOneRelatedField, ManyToManyRelatedField
from common.mixins import NestedSerializerMixin
from sor.models import (
    Label,
    Owner,
    Cluster,
    Environment,
    Domain,
    OperatingSystem,
    Server,
    Product,
)


class LabelSerializer(serializers.ModelSerializer):
    """Serializes Label model
    """

    class Meta:
        model = Label
        fields = [
            "id",
            "name",
        ]


class OwnerSerializer(serializers.ModelSerializer):
    """Serializes Owner model
    """

    class Meta:
        model = Owner
        fields = [
            "id",
            "name",
            "email",
            "description",
        ]


class ClusterSerializer(serializers.ModelSerializer):
    """Serializes Cluster model
    """

    class Meta:
        model = Cluster
        fields = [
            "id",
            "name",
            "description",
        ]


class EnvironmentSerializer(serializers.ModelSerializer):
    """Serializes Environment model
    """

    class Meta:
        model = Environment
        fields = [
            "id",
            "name",
            "category",
            "description",
        ]


class DomainSerializer(serializers.ModelSerializer):
    """Serializes Domain model
    """

    owner = ManyToOneRelatedField()

    class Meta:
        model = Domain
        fields = [
            "id",
            "name",
            "location",
            "owner",
            "description",
            "status",
        ]

    def create(self, validated_data):
        return Domain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def validate_owner(self, value):
        try:
            owner = Owner.objects.get(name=value)
        except Owner.DoesNotExist:
            msg = "Owner %s matching query does not exist" % value
            raise ValidationError([msg])
        return owner


class OperatingSystemSerializer(serializers.ModelSerializer):
    """Serializes OperatingSystem model
    """

    class Meta:
        model = OperatingSystem
        fields = [
            "id",
            "name",
            "family",
            "architecture",
            "version",
        ]


class ServerSerializer(serializers.ModelSerializer, NestedSerializerMixin):
    """Serializes Server model
    """

    owner = ManyToOneRelatedField()
    domain = ManyToOneRelatedField()
    cluster = ManyToOneRelatedField()
    environments = ManyToManyRelatedField()
    operating_system = ManyToOneRelatedField()
    labels = ManyToManyRelatedField()

    class Meta:
        model = Server
        fields = [
            "id",
            "name",
            "ip_address",
            "category",
            "owner",
            "domain",
            "cluster",
            "environments",
            "operating_system",
            "labels",
            "description",
            "status",
        ]

    def validate_owner(self, value):
        try:
            owner = Owner.objects.get(name=value)
        except Owner.DoesNotExist:
            msg = "Owner %s matching query does not exist" % value
            raise ValidationError([msg])
        return owner

    def validate_domain(self, value):
        try:
            domain = Domain.objects.get(name=value)
        except Domain.DoesNotExist:
            msg = "Domain %s matching query does not exist" % value
            raise ValidationError([msg])
        return domain

    def validate_cluster(self, value):
        try:
            cluster = Cluster.objects.get(name=value)
        except Cluster.DoesNotExist:
            msg = "Cluster %s matching query does not exist" % value
            raise ValidationError([msg])
        return cluster

    def validate_environments(self, value):
        environments = []

        for environment_name in value:
            try:
                environments.append(
                    Environment.objects.get(name=environment_name)
                )
            except Environment.DoesNotExist:
                msg = (
                    "Environment %s matching query does not exist"
                    % environment_name
                )
                raise ValidationError([msg])
        return environments

    def validate_operating_system(self, value):
        try:
            operating_system = OperatingSystem.objects.get(name=value)
        except OperatingSystem.DoesNotExist:
            msg = "OperatingSystem %s matching query does not exist" % value
            raise ValidationError([msg])
        return operating_system

    def validate_labels(self, value):
        labels = []

        for label_name in value:
            try:
                labels.append(Label.objects.get(name=label_name))
            except Label.DoesNotExist:
                msg = "Label %s matching query does not exist" % label_name
                raise ValidationError([msg])
        return labels


class ProductSerializer(serializers.ModelSerializer):
    """Serializes Product model
    """

    owner = ManyToOneRelatedField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "port",
            "version",
            "owner",
            "link",
            "repository",
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def validate_owner(self, value):
        try:
            owner = Owner.objects.get(name=value)
        except Owner.DoesNotExist:
            msg = "Owner %s matching query does not exist" % value
            raise ValidationError([msg])
        return owner
