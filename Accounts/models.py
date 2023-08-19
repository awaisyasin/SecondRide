from typing import Any, Dict, Tuple
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    def delete(self, *args, **kwargs):
        # Perform any pre-delete operations or custom logic here

        # Call super() to invoke the default delete behavior
        super().delete(*args, **kwargs)