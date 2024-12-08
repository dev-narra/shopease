from shop.models import User, Product, Order, OrderItem, Payment, Feedback

def run():
    # customer = User.objects.create(email="customer9@example.com",username="customer9", password="password126", is_customer=True)

    # product5 = Product.objects.create(
    #     name="party dress",
    #     description="The party look.....",
    #     price=999.99,
    #     mfg_date="2024-01-01",
    #     exp_date="2025-01-01",
    #     category="Cloth",
    #     stock_quantity=10
    # )
    

    # payment1=Payment.objects.create(customer=customer,amount=999.99, method="PayPal")

    # order = Order.objects.create(customer=customer,product=product5,payment=payment1,status="Pending",order_datetime="2024-12-20",exp_delivery_date="2024-12-25")

    # OrderItem.objects.create(order=order, product=product5, quantity=1)
    
    # Feedback.objects.create(product=product5, customer=customer, rating=4.3, review="Excellent!")


# Create a user
        customer = User.objects.create_user(
            email="customer123@example.com",
            username="customer21",
            password="password120",
            is_customer=True
        )

        # Verify user creation
        print(f"Customer created: {customer} with ID {customer.id}")

        # Create a payment for the customer
        payment1 = Payment.objects.create(
            amount=999.99,
            method="PayPal",
            paid_by=customer
        )
        print(f"Payment created: {payment1}")
