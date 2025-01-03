from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.interactors.storage_interfaces.storage_interface import AuthTokenDto,ProductDto,CustomerDto,PaymentDto,FeedbackDto,OrderDto,OrderStatusDto,CancelOrderDto
from shop.constants.exception_messages import INVALID_STOCK_VALUE,INVALID_ORDER_STATUS,INVALID_ORDER_ID,ORDER_ID_DOES_NOT_EXISTS,INVALID_FEEDBACK_ID,FEEDBACK_ID_DOES_NOT_EXISTS,PRODUCT_ID_DOES_NOT_EXISTS,CUSTOMER_ID_DOES_NOT_EXISTS,INVALID_EMAIL,INVALID_CUSTOMER_EMAIL,INVALID_CUSTOMER_PHONE,INVALID_CUSTOMER_ADDRESS,INVALID_CUSTOMER_NAME,CUSTOMER_ALREADY_EXISTS,INVALID_CUSTOMER_ID,INAVLID_LIMIT_VALUE,INAVLID_OFFSET_VALUE,INVALID_DESCRIPTION,INVALID_PRICE,INVALID_MFG_DATE,INVALID_EXP_DATE,INVALID_CATEGORY,INVALID_STOCK_QUANTITY,INVALID_PRODUCT_NAME,PRODUCT_NAME_ALREADY_EXISTS,INVALID_PRODUCT_ID,INVALID_PAYMENT_AMOUNT,INVALID_PAYMENT_METHOD,INVALID_PAYMENT_TRANSACTION_DATE,INVALID_PAYMENT_ID,INVALID_RATING,INVALID_REVIEW

from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List

class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_email(self):
        raise NotFound(*INVALID_EMAIL)

    def get_response_for_user_login(self,auth_tokens:AuthTokenDto):
        return{
            "access_token":auth_tokens.access_token,
            "expires_in":auth_tokens.expires_in
        }
    
    def raise_exception_for_invalid_product_name(self):
        raise NotFound(*INVALID_PRODUCT_NAME)

    def raise_exception_for_invalid_product_name_exists(self):
        raise NotFound(*PRODUCT_NAME_ALREADY_EXISTS)

    def raise_exception_for_invalid_description(self):
        raise NotFound(*INVALID_DESCRIPTION)

    def raise_exception_for_invalid_price(self):
        raise NotFound(*INVALID_PRICE)

    def raise_exception_for_invalid_exp_date(self):
        raise NotFound(*INVALID_EXP_DATE)

    def raise_exception_for_invalid_mfg_date(self):
        raise NotFound(*INVALID_MFG_DATE)

    def raise_exception_for_invalid_category(self):
        raise NotFound(*INVALID_CATEGORY)

    def raise_exception_for_invalid_stock_quantity(self):
        raise NotFound(*INVALID_STOCK_QUANTITY)
    
    def get_response_for_create_product(self,product_id:int)->int:
        return {
            "product_id":product_id
        }
    
    def get_response_for_get_products(self,products:list[ProductDto]):
        products_array = [
        {
            "name": product.name,
            "description": product.description,
            "price": float(product.price),
            "mfg_date": str(product.mfg_date),
            "exp_date": str(product.exp_date),
            "category": product.category,
            "stock_quantity": product.stock_quantity,
            "id": product.id
        }
        for product in products]
        return products_array

    def get_response_for_create_customer(self,customer_id:int)->int:
        return{
            "customer_id":customer_id
        }

    def get_response_for_search_products(self,products:list[ProductDto]):
        products_array = [
        {
            "name": product.name,
            "description": product.description,
            "price": float(product.price),
            "mfg_date": str(product.mfg_date),
            "exp_date": str(product.exp_date),
            "category": product.category,
            "stock_quantity": product.stock_quantity,
            "id": product.id
        }
        for product in products]
        return products_array

    def raise_exception_for_invalid_customer_email(self):
        raise NotFound(*INVALID_CUSTOMER_EMAIL)

    def raise_exception_for_invalid_customer_phone(self):
        raise NotFound(*INVALID_CUSTOMER_PHONE)

    def raise_exception_for_invalid_customer_address(self):
        raise NotFound(*INVALID_CUSTOMER_ADDRESS)

    def raise_exception_for_invalid_customer_name(self):
        raise NotFound(*INVALID_CUSTOMER_NAME)

    def raise_exception_for_customer_alredy_exists(self):
        raise NotFound(*CUSTOMER_ALREADY_EXISTS)


    def get_response_for_update_customer(self,customer:CustomerDto):
        return {
            "id":customer.id,
            "name":customer.name,
            "email":customer.email,
            "phone":customer.phone,
            "address":customer.address
        }

    def raise_exception_for_invalid_customer_id(self):
        raise NotFound(*INVALID_CUSTOMER_ID)

    def get_response_for_gets_the_customers(self,customers:list[CustomerDto]):
        customers_array=[
            {
                "id":customer.id,
                "name":customer.name,
                "email":customer.email,
                "phone":customer.phone,
                "address":customer.address
            }
            for customer in customers
        ]
        return customers_array

    def raise_exception_for_invalid_limit_value(self):
        raise NotFound(*INAVLID_LIMIT_VALUE)

    def raise_exception_for_invalid_offset_value(self):
        raise NotFound(*INAVLID_OFFSET_VALUE)
    
    def get_response_for_search_customers(self,customers:list[CustomerDto]):
        customers_array=[
            {
                "id":customer.id,
                "name":customer.name,
                "email":customer.email,
                "phone":customer.phone,
                "address":customer.address
            }
            for customer in customers
        ]
        return customers_array

    def get_response_for_delete_product(self)->str:
        return {
            "message":"Product is deleted............."
        }
    
    def raise_exception_for_invalid_product_id(self):
        raise NotFound(*INVALID_PRODUCT_ID)

    def get_response_for_create_payment(self,payment_id:int)->int:
        return{
            "payment_id":payment_id
        }
    
    def raise_exception_for_invalid_payment_amount(self):
        raise NotFound(*INVALID_PAYMENT_AMOUNT)

    def raise_exception_for_invalid_payment_method(self):
        raise NotFound(*INVALID_PAYMENT_METHOD)

    def raise_exception_for_invalid_payment_transaction_date(self):
        raise NotFound(*INVALID_PAYMENT_TRANSACTION_DATE)

    def get_response_for_get_payments(self,payments:list[PaymentDto]):
        payments_array=[
            {
               "id":payment.id,
               "amount":float(payment.amount),
               "method":payment.method,
               "transaction_date":str(payment.transaction_date)
            }
            for payment in payments
        ]
        return payments_array

    def get_response_for_update_payment(self,payment:PaymentDto):
        return{
            "id":payment.id,
            "amount":payment.amount,
            "method":payment.method,
            "transaction_date":payment.transaction_date
        }

    def raise_exception_for_invalid_payment_id(self,payment_id:int):
        raise NotFound(*INVALID_PAYMENT_ID)

    def get_response_for_update_product(self,product:ProductDto):
        return{
            "id":product.id,
            "description": product.description,
            "price": product.price,
            "mfg_date":product.mfg_date,
            "exp_date": product.exp_date,
            "category": product.category,
            "stock_quantity": product.stock_quantity,
        }

    def get_response_for_delete_customer(self)->str:
        return {
            "message":"Customer is deleted............."
        }

    def get_response_for_add_product_feedback(self,feedback:FeedbackDto):
        return{
            "rating":feedback.rating,
            "review":feedback.review
        }

    def raise_exception_for_invalid_rating(self):
        raise NotFound(*INVALID_RATING)

    def raise_exception_for_invalid_review(self):
        raise NotFound(*INVALID_REVIEW)

    def raise_exception_for_customer_id_does_not_exists(self):
        raise NotFound(*CUSTOMER_ID_DOES_NOT_EXISTS)

    def raise_exception_for_product_id_does_not_exists(self):
        raise NotFound(*PRODUCT_ID_DOES_NOT_EXISTS)

    def raise_exception_for_feedback_id_does_not_exists(self):
        raise NotFound(*FEEDBACK_ID_DOES_NOT_EXISTS)

    def get_response_for_delete_feedback(self)->str:
        return{
            "message":"Feedabck is deleted............."
        }
    
    def get_response_for_gets_the_feedbacks(self,feedbacks:list[FeedbackDto]):
        feedbacks_array=[
            {
              "rating":feedback.rating,
              "review":feedback.review
            }
            for feedback in feedbacks
        ]
        return feedbacks_array

    def get_response_for_update_feedback(self,feedback:FeedbackDto):
        return{
            "rating":feedback.rating,
            "review":feedback.review
        }

    def raise_exception_for_invalid_feedback_id(self):
        raise NotFound(*INVALID_FEEDBACK_ID)

    def raise_exception_for_invalid_order_id(self):
        raise NotFound(*INVALID_ORDER_ID)

    def raise_exception_for_order_id_not_exists(self):
        raise NotFound(*ORDER_ID_DOES_NOT_EXISTS)

    def get_response_for_cancel_order(self,order:CancelOrderDto):
        return{
            "message":"Order status changed",
            "orderId":order.id,
            "status":order.status
        }

    def raise_exception_for_invalid_order_status(self):
        raise NotFound(*INVALID_ORDER_STATUS)
    
    def get_response_for_update_order_status(self,order:OrderStatusDto):
        return{
            "message":"Order status updated successfully...........",
            "orderId":order.id,
            "newStatus":order.status
        }

    def get_response_for_get_orders_list(self,orders:list[OrderDto]):
        order_array=[
            {
              "customer_id":order.customer_id,
              "payment_id":order.payment_id,
              "status":order.status,
              "order_datetime":str(order.order_datetime),
              "expected_delivery_date":str(order.exp_delivery_date)
            }
            for order in orders
        ]
        return order_array

    def get_response_for_search_orders(self,orders:list[OrderDto]):
        orders_array=[
            {
              "customer_id":order.customer_id,
              "payment_id":order.payment_id,
              "status":order.status,
              "order_datetime":order.order_datetime,
              "expected_delivery_date":order.exp_delivery_date
            }
            for order in orders
        ]
        return orders_array

    def get_response_for_low_stock_products(self,products:list[ProductDto]):
        products_array=[
            {
              "id":product.id,
              "name":product.name,
              "description":product.description,
              "price":float(product.price),
              "mfg_date":str(product.mfg_date),
              "exp_date":str(product.exp_date),
              "category":product.category,
              "stock_quantity":product.stock_quantity
            }
            for product in products
        ]
        return products_array

    def raise_exception_for_invalid_stock_value(self):
        raise NotFound(*INVALID_STOCK_VALUE)
        