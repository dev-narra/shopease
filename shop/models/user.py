from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
