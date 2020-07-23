from django.db import models

# Create your models here.

"""Core Vault:

SecretItem (Useful for variables)
* id
* name
* Value
* Labels/Scope/Tag (Many-to-Many)

SecretLogin (Useful for credentials)
* id
* name
* username
* password
* link (foreignkey, one-to-many)
* Labels/Scope/Tag (Many-to-Many)

SecretNotes (Useful for any notes or may be ssh public key or something)
* id
* name
* note
* Labels/Scope/Tag  (Many-to-Many)

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
