from shop.interactors.storage_interfaces.storage_interface import StorageInterface,AuthTokenDto,ProductDto,CustomerDto,PaymentDto,FeedbackDto,OrderDto
from ib_users.interfaces.service_interface import ServiceInterface
from shop.exceptions.custom_exceptions import InvalidFeedbackId,FeedbackIdDoesNotExists,InvalidCustomePhone,InvalidCustomerAddress,InvalidCustomerEmail,InvalidCustomerName,InvalidEmail,CustomerAlreadyExist,InvalidLimitValue,InvalidProductId,InvalidOffsetValue,InvalidProductName,InvalidDescription,InvalidCategory,InvalidPrice,InvalidExpDate,InvalidMfgDate,InvalidStockQuantity,CustomerIdDoesNotExists,ProductIdDoesNotExists,InvalidReview,InvalidRating
from shop.models import User,Product,Customer,Payment,Feedback
from typing import List
from django.db.models import Q



class StorageImplementation(StorageInterface):
       def validate_email(self,email:str):
         is_valid_email=User.objects.filter(email=email).exists()
         is_invalid_email=not is_valid_email
         if is_invalid_email:
            raise InvalidEmail
       
       def user_login(self,email:str)->AuthTokenDto:
          user = User.objects.get(email=email).id
          service_interface = ServiceInterface()
          auth_tokens = service_interface.create_auth_tokens_for_user(user)
          return auth_tokens
       
       def validate_product_name(self,name:str):
         is_product_name_exist=name is not None
         if not is_product_name_exist:
            raise InvalidProductName

       def validate_product_name_exists(self,name:str):
         is_product_name_exist=Product.objects.filter(name=name).exists()
         if is_product_name_exist:
            raise ProductNameAlreadyExists

       def validate_description(self,description:str):
         is_valid_description=description is not None
         if not is_valid_description:
            raise InvalidDescription
       
       def validate_price(self,price:float):
         is_valid_price=price is not None
         if not is_valid_price:
            raise InvalidPrice

       def validate_mfg_date(self,mfg_date:str):
         is_valid_mfg_date=mfg_date is not None
         if not is_valid_mfg_date:
            raise InvalidMfgDate

       def validate_exp_date(self,exp_date:str):
         is_valid_exp_date=exp_date is not None
         if not is_valid_exp_date:
            raise InvalidExpDate

       def validate_category(self,category:str):
         is_valid_category=category is not None
         if not is_valid_category:
            raise InvalidCategory
       
       def validate_stock_quantity(self,stock_quantity:int):
         is_valid_stock_quantity=stock_quantity is not None
         if not is_valid_stock_quantity:
            raise InvalidStockQuantity
       
       def create_product(self,name:str,description:str,price:float,mfg_date:str,exp_date:str,category:str,stock_quantity:int)->ProductDto:
          product=Product.objects.create(name=name,description=description,price=price,mfg_date=mfg_date,exp_date=exp_date,category=category,stock_quantity=stock_quantity)
          product_id=product.id
          return product_id


       def get_products(self,limit:int,offset:int)->list[ProductDto]:
          products=Product.objects.all()[offset:offset+limit]
          return products

       def validate_customer(self,email:str):
         is_customer_exist=Customer.objects.filter(email=email).exists()
         if is_customer_exist:
            raise CustomerAlreadyExist

      
       def validate_customer_name(self,name:str):
         is_valid_customer_name=name is not None
         is_invalid_customer_name=not is_valid_customer_name
         if is_invalid_customer_name:
            raise InvalidCustomerName

       def validate_customer_email(self,email:str):
         is_valid_customer_email=email is not None
         is_invalid_customer_email=not is_valid_customer_email
         if is_invalid_customer_email:
            raise InvalidCustomerEmail

       def validate_customer_phone(self,phone:str):
         is_valid_phone=phone is not None and len(phone)==10
         is_invalid_customer_phone=not is_valid_phone
         if is_invalid_customer_phone:
            raise InvalidCustomePhone

       def validate_customer_address(self,address:str):
         is_valid_customer_address=address is not None
         is_invalid_customer_address=is_valid_customer_address
         if is_invalid_customer_address:
            raise InvalidCustomerAddress

       def validate_customer_id(self,id:int):
         is_valid_customer_id=id is not None
         invalid_customer_id=not is_valid_customer_id
         if invalid_customer_id:
            raise InvalidCustomerId

       def create_customer(self,name:str,email:str,phone:str,address:str)->int:
          customer=Customer.objects.create(name=name,email=email,phone=phone,address=address)
          customer_id=customer.id
          return customer_id

       def search_products(self,name:str,category:str)->list[ProductDto]:
         if name or category:
            products = Product.objects.filter(
                Q(name__icontains=name) | Q(category__icontains=category)
            )
            return products
      
       def update_customer(self,id:int,name:str,email:str,phone:str,address:str)->CustomerDto:
         customer=Customer.objects.get(id=id)
         customer.id=id
         customer.name=name
         customer.email=email
         customer.phone=phone,
         customer.address=address
         customer.save()
         
         return customer
         
       def get_customers(self,limit:int,offset:int)->list[CustomerDto]:
         customers=Customer.objects.all()[offset:offset+limit]
         return customers

       def validate_limit_value(self,limit:int):
           valid_limit_value=limit is not None and limit >=1
           if not valid_limit_value:
               raise InvalidLimitValue

       def validate_offset_value(self,offset:int):
           valid_offset_value=offset is not None
           if not valid_offset_value:
               raise InvalidOffsetValue
         
       def search_customers(self,name:str,email:str)->list[CustomerDto]:
            if name or email:
               customers = Customer.objects.filter(
                  Q(name__icontains=name) | Q(email__icontains=email)
               )
               return customers
            
       def delete_product(self,id:int)->str:
           product=Product.objects.get(id=id)
           product.delete()
           
       def validate_product_id(self,id:int):
         is_valid_product_id=id is not None
         invalid_product_id=not is_valid_product_id
         if invalid_product_id:
            raise InvalidProductId

       def create_payment(self,amount:float,method:str,transaction_date:str)->PaymentDto:
         payment=Payment.objects.create(amount=amount,method=method,transaction_date=transaction_date)
         payment_id:payment.id
         return payment_id

       def validate_payment_amount(self,amount:float):
         is_valid_amount=amount is not None and amount>0
         if not is_valid_amount:
            raise InvalidPaymentAmount

       
       def validate_payment_method(self,method:str):
         is_valid_method=method is not None
         if not is_valid_method:
            raise InvalidPaymentMethod

       def validate_payment_transaction_date(self,transaction_date:str):
         is_valid_transaction_date=transaction_date is not None
         if not is_valid_transaction_date:
            raise InvalidPaymentTransactionDate

       def get_payments(self,limit:int,offset:int)->list[PaymentDto]:
         payments=Payment.objects.all()[offset:offset+limit]
         return payments

       def update_payment(self,payment_id:int,amount:float,method:str,transaction_date:str)->PaymentDto:
         payment=Payment.objects.get(id=payment_id)
         payment.id=payment_id
         payment.amount=amount
         payment.method=method
         payment.transaction_date=transaction_date
         payment.save()

         return payment
      
       def validate_payment_id(self,payment_id:int):
         is_payment_id_exists=Payment.objects.filter(id=payment_id).exists()
         if not is_payment_id_exists:
            raise InvalidPaymentId
      
       def update_product(self,product_id:int,name:str,description:str,price:float,mfg_date:str,exp_date:str,category:str,stock_quantity:int)->ProductDto:
            product=Product.objects.get(id=product_id)
            product.name=name
            product.description=description
            product.price=price
            product.mfg_date=mfg_date
            product.exp_date=exp_date
            product.category=category
            product.stock_quantity=stock_quantity
            product.save()

            return product

       def validate_product_id(self,product_id:int):
         is_valid_product_id=product_id is not None
         if not is_valid_product_id:
            raise InvalidProductId

       def delete_customer(self,customer_id:int)->str:
         customer=Customer.objects.get(id=customer_id)
         customer.delete()

       def add_product_feedback(self,product_id:int,customer_id:int,rating:float,review:str)->FeedbackDto:
           product=Product.objects.get(id=product_id)
           customer=Customer.objects.get(id=customer_id)
           feedback=Feedback.objects.create(product=product,customer=customer,rating=rating,review=review)
           return feedback

       def validate_rating(self,rating:float):
          is_valid_rating=rating is not None and rating<=5.0
          if not is_valid_rating:
            raise InvalidRating
       
       def validate_review(self,review:str):
         is_valid_review=review is not None
         if not is_valid_review:
          raise InvalidReview

       def validate_customer_id_exists(self,customer_id:int):
         is_valid_customer=Customer.objects.filter(id=customer_id).exists()
         if not is_valid_customer:
          raise CustomerIdDoesNotExists

       def validate_product_id_exists(self,product_id:int):
        is_valid_product=Product.objects.filter(id=product_id).exists()
        if not is_valid_product:
          raise ProductIdDoesNotExists

       def validate_feedback_id_exists(self,feedback_id:int):
        is_valid_feedback=Feedback.objects.filter(id=feedback_id).exists()
        if not is_valid_feedback:
          raise FeedbackIdDoesNotExists

       def delete_feedback(self,feedback_id:int)->str:
         feedback=Feedback.objects.get(id=feedback_id)
         feedback.delete()

       def get_feedbacks(self,limit:int,offset:int)->list[FeedbackDto]:
         feedbacks=Feedback.objects.all()[offset:offset+limit]
         return feedbacks

       def update_feedback(self,feedback_id:int,rating:float,review:str)->FeedbackDto:
          feedback=Feedback.objects.get(id=feedback_id)
          feedback.rating=rating
          feedback.review=review
          feedback.save()

          return feedback

       def validate_feedback_id(self,feedback_id:int):
          is_valid_feedback_id=feedback_id is not None and type(feedback_id)==int
          if not is_valid_feedback_id:
            raise InvalidFeedbackId

       def validdate_order_id(self,order_id:int):
         is_valid_order_id=order_id is not None
         if not is_valid_order_id:
          raise InvalidOrderId

       def validate_order_id_exists(self,order_id:int):
        is_order_id_exists=Order.objects.get(id=order_id).exist()
        if not is_order_id_exists:
          raise OrderIdDoesNotExist

       def cancel_order(self,order_id:int):
        order=Order.objects.get(id=order_id)
        order.status="Canceled"
        order.save()
        
        return order
      