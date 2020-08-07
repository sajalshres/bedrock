from rest_framework.serializers import Field
from rest_framework.exceptions import ValidationError


class ManyToOneRelatedField(Field):
    """ManytoOne related custom serializer field

    TODO: Add Unit Test
    """

    def to_representation(self, related_field):
        return related_field.name

    def to_internal_value(self, data):
        if not isinstance(data, str):
            msg = "Incorrect Type. Expected a str but got %s" % (
                type(data).__name__
            )
            raise ValidationError([msg])

        if not data:
            msg = "%s value cannot be empty" % (self.field_name)
            raise ValidationError([msg])

        return data


class ManyToManyRelatedField(Field):
    """ManytoMany related custom serializer field

    TODO: Add Unit Test
    """

    def to_representation(self, related_field):
        return [item.name for item in related_field.all()]

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
