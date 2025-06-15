from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPES = (
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
)


class CustomUser(AbstractUser):
    user_type = models.CharField(
        max_length=10, choices=USER_TYPES, default='Patient'
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True
    )
    address_line1 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    