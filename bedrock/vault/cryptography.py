import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from django.conf import settings
from django.utils.encoding import force_bytes


class Cryptography:
    """Cryptography package to encrypt and decrypt secrets
    """

    def __init__(self, password=None):
        if password is None:
            password = getattr(settings, "VAULT_KEY", None) or getattr(
                settings, "SECRET_KEY"
            )
        assert len(password) >= 32, "vault key length must be more than 32"
        self.password = password

    @property
    def kdf(self):
        return PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.urandom(16),
            iterations=100000,
            backend=default_backend(),
        )

    @property
    def password(self):
        return base64.urlsafe_b64encode(self.kdf.derive(self._password))

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def fernet(self):
        return Fernet(key=self.password)

    def encrypt(self, message):
        return self.fernet.encrypt(force_bytes(message))

    def decrypt(self, encrypted_message):
        return self.fernet.decrypt(token=encrypted_message)
