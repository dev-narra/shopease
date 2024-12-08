from django.db import models
from .user import User

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)
    

