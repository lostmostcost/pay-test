from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bank_account = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username