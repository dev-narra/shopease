from django.db import models
from .user import User
from .product import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_customer': True})
    products = models.ManyToManyField(Product, through='OrderItem')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    order_datetime = models.DateTimeField(auto_now_add=True)
    exp_delivery_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.email}"