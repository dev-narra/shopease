from django.db import models
from .product import Product
from .user import User



class Feedback(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='feedback')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    rating = models.FloatField()
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.customer.email} for {self.product.name}"