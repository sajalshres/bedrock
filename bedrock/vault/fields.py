from django.db import models
from rest_framework.serializers import Field
from rest_framework.exceptions import ValidationError

from vault.mixins import EncryptedFieldMixin


class URLListField(Field):
    """URL related custom serializer field

    TODO: Add Unit Test
    """

    def to_representation(self, related_field):
        return related_field.values_list("url", flat=True)

    def to_internal_value(self, data):
        if not isinstance(data, list):
            msg = "Incorrect Type. Expected a list but got %s" % (
                type(data).__name__
            )
            raise ValidationError([msg])

        if not all(isinstance(item, str) for item in data):
            msg = "Incorrect Value Type. Expected %s value in str type" % (
                self.source
            )
            raise ValidationError([msg])

        return data


class EncryptedCharField(EncryptedFieldMixin, models.CharField):
    pass
