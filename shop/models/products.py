from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mfg_date = models.DateField(null=True,blank=True)
    exp_date = models.DateField(null=True,blank=True)
    category = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name