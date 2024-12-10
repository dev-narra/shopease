from shop.models import User,Customer, Product, Order, OrderItem, Payment, Feedback

def run():
    
    customer = User.objects.create(email="deva@gamil.com",username="dev")

    product5 = Product.objects.create(
        name="party dress",
        description="The party look.....",
        price=999.99,
        mfg_date="2024-01-01",
        exp_date="2025-01-01",
        category="Cloth",
        stock_quantity=10
    )
    

    payment1=Payment.objects.create(amount=999.99, method="PayPal",transaction_date="2024-12-12")

    order = Order.objects.create(customer=customer,product=product5,payment=payment1,status="Pending",order_datetime="2024-12-20",exp_delivery_date="2024-12-25")

    OrderItem.objects.create(order=order, product=product5, quantity=1)
    
    Feedback.objects.create(product=product5, customer=customer, rating=4.3, review="Excellent!",created_at="2024-12-12")

