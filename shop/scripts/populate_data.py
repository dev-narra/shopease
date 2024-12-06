from shop.models import User, Product, Order, OrderItem, Payment, Feedback

def run():
    customer = User.objects.create_user(email="customer6@example.com",username="customer6", password="password126", is_customer=True)

    product5 = Product.objects.create(
        name="party dress",
        description="The party look.....",
        price=999.99,
        mfg_date="2024-01-01",
        exp_date="2025-01-01",
        category="Cloth",
        stock_quantity=10
    )

    order = Order.objects.create(customer=customer, status="Pending")
    OrderItem.objects.create(order=order, product=product5, quantity=1)

    Payment.objects.create(order=order, amount=999.99, method="PayPal")

    Feedback.objects.create(product=product5, customer=customer, rating=4.3, review="Excellent!")
