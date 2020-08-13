"""Common mixins for vault api
"""

from django.db import models

from vault.exceptions import EncryptedFieldException
from vault.cryptography import Cryptography


class EncryptedFieldMixin(models.Field):
    internal_type = "CharField"
    prepared_max_length = None

    def __init__(self, key=None, **kwargs):
        kwargs.setdefault("max_length", self.prepared_max_length)
        self.cryptography = Cryptography(key)
        super().__init__(**kwargs)

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared=prepared)
        if value is not None:
            encrypted_value = self.cryptography.encrypt(value)
            if self.max_length and len(encrypted_value) > self.max_length:
                raise EncryptedFieldException(
                    f"Max length exceeded for encrypted field {self.name}"
                )
            return encrypted_value
        return None

    def from_db_value(self, value, expression, connection, *args):
        if value is not None:
            return self.to_python(self.cryptography.decrypt(value))
        return None

    def get_internal_type(self):
        return self.internal_type
