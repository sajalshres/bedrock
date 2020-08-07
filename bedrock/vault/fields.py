from rest_framework.serializers import Field
from rest_framework.exceptions import ValidationError


class URLListField(Field):
    """URL related custom serializer field

    TODO: Add Unit Test
    """

    def to_representation(self, related_field):
        return related_field.values_list("url", flat=True)

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

