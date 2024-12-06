from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,Group


# User model
class User(AbstractUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set'  
    )

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  
        blank=True,
    )


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

