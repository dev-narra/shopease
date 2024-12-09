from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, help_text="The full name of the customer.")
    email = models.EmailField(unique=True, help_text="The email address of the customer.")
    phone = models.CharField(
        max_length=15,
        unique=True,
        help_text="The phone number of the customer, including country code."
    )
    address = models.TextField(help_text="The physical address of the customer.")

