from django.db import models
import uuid

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid1, editable=False, unique=True)
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)