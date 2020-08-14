from django.db import models
from sor.models import Label

from vault.fields import EncryptedCharField

# Create your models here.

"""Core Vault:

Custom Fields can be attached to any of the Core Tables:

CustomTextField
* id
* key
* value

CustomSecretField
* id
* key
* secret

CustomBooleanField
* id
* key
* boolean

Assumptions:
* All logged in users can access the credentials.(As its restricted to DevOps)
* Secrets will be encrypted using a shared-master key.
* API will return the secrets encrypted with user-password for security.
* client will again de-crypt the values. Examples will be provided.
"""


class SecretItem(models.Model):
    """Items useful for variables
    """

    title = models.CharField(max_length=253)
    name = models.CharField(max_length=253)
    value = models.CharField(max_length=253)
    note = models.TextField(null=True, blank=True)
    labels = models.ManyToManyField(Label, related_name="secret_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def type(self):
        return "item"


class SecretLogin(models.Model):
    """Secret logins useful for storing encrypted credentials
    """

    title = models.CharField(max_length=253)
    username = models.CharField(max_length=253)
    password = EncryptedCharField(max_length=253)
    note = models.TextField(null=True, blank=True)
    labels = models.ManyToManyField(Label, related_name="secret_logins")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def type(self):
        return "login"


class SecretNotes(models.Model):
    """Secret notes useful for storing long text notes like ssh keys
    """

    title = models.CharField(max_length=253)
    note = models.TextField()
    labels = models.ManyToManyField(Label, related_name="secret_notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def type(self):
        return "note"


class Link(models.Model):
    """Links used for secret logins
    """

    url = models.URLField(max_length=253)
    secret_login = models.ForeignKey(
        SecretLogin, related_name="links", on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
