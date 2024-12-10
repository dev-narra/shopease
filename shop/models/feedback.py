from django.db import models
from .products import Product
from .customer import Customer

class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Feedback by {self.customer.email} for {self.product.name}"