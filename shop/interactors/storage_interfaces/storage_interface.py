from abc import abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass()
class AuthTokenDto:
    access_token:str
    expires_in:float

@dataclass()
class ProductDto:
    name:str
    description:str
    price:float
    mfg_date:str
    exp_date:str
    category:str
    stock_quantity:int

@dataclass()
class CustomerDto:
    id:int
    name:str
    email:str
    phone:str
    address:str

@dataclass()
class PaymentDto:
    id:int
    amount:float
    amount:str
    transaction_date:str

@dataclass()
class OrderDto:
    customer_id:int
    payment_id:int
    status:str
    order_datetime:str
    expected_delivery_date:str
@dataclass()
class CancelOrderDto:
    message:str
    orderId:int
    status:str
    

@dataclass()
class FeedbackDto:
    customer_id:int
    rating:float
    review:float

@dataclass()
class OrderStatusDto:
    message:str
    orderId:int
    newStatus:str

class StorageInterface:

    @abstractmethod
    def validate_email(self,email:str):
        pass

    @abstractmethod
    def user_login(self,email:str)->AuthTokenDto:
        pass
   
    @abstractmethod
    def get_products(self,limit:int,offset:int)->list[ProductDto]:
        pass
    
    @abstractmethod
    def validate_name(self,name:str):
        pass

    @abstractmethod
    def validate_description(self,description:str):
        pass

    @abstractmethod
    def validate_price(self,price:float):
        pass

    @abstractmethod
    def validate_exp_date(self,exp_date:str):
        pass

    @abstractmethod
    def validate_mfg_date(self,mfg_date:str):
        pass
    
    @abstractmethod
    def validate_category(self,category:str):
        pass

    @abstractmethod
    def validate_stock_quantity(self,stock_quantity:str):
        pass
    
    @abstractmethod
    def validate_product_name(self,name:str):
        pass
    
    @abstractmethod
    def validate_product_name_exists(self,name:str):
        pass
    

    @abstractmethod
    def create_product(self):
        pass


    @abstractmethod
    def validate_customer(self,email:str):
        pass
    
    @abstractmethod
    def validate_customer_name(self,name:str):
        pass

    @abstractmethod
    def validate_customer_email(self,email:str):
        pass
    
    @abstractmethod
    def validate_customer_phone(self,email:str):
        pass

    @abstractmethod
    def validate_customer_address(self,email:str):
        pass

    @abstractmethod
    def validate_input_data(self,name:str,email:str,phone:str,address:str):
        pass
    
    @abstractmethod
    def create_customer(self,name:str,email:str,phone:str,address:str)->int:
        pass


    @abstractmethod
    def search_products(self,name:str,category:str)->List[ProductDto]:
        pass

    @abstractmethod
    def validate_customer_id(self,id:int):
        pass

    @abstractmethod   
    def update_customer(self,id:int,name:str,email:str,phone:str,address:str)->CustomerDto:
        pass
    

    @abstractmethod
    def get_customers(self,limit:int,offset:int)->list[CustomerDto]:
        pass

    @abstractmethod
    def validate_limit_value(self,limit:int):
        pass

    @abstractmethod
    def validate_offset_value(self,offset:int):
        pass

    @abstractmethod
    def search_customers(self,name:str,email:str):
        pass
    
    @abstractmethod
    def delete_product(self,id:int)->int:
        pass
    
    @abstractmethod
    def validate_product_id(self,product_id:int):
        pass

    @abstractmethod
    def create_payment(self,amount:float,method:str,transaction_date:str)->PaymentDto:
        pass

    @abstractmethod
    def validate_payment_amount(self,amount:float):
        pass

    @abstractmethod
    def validate_payment_method(self,method:str):
        pass

    @abstractmethod
    def validate_payment_transaction_date(self,transaction_date:str):
        pass

    @abstractmethod
    def get_payments(self,limit:int,offset:int):
        pass

    @abstractmethod
    def update_payment(self,amount:float,method:str,transaction_date:str)->PaymentDto:
        pass

    @abstractmethod
    def validate_payment_id(self,payment_id:int):
        pass
    
    @abstractmethod
    def update_product(self,product_id:int,name:str,description:str,price:float,mfg_date:str,exp_date:str,category:str,stock_quantity:int)->ProductDto:
        pass

    @abstractmethod
    def validate_product_id(self,product_id:int):
        pass

    @abstractmethod
    def delete_customer(self,customer_id:int):
        pass

    @abstractmethod
    def add_product_feedback(self,product_id:int,customer_id:int,rating:float,review:str)->FeedbackDto:
        pass

    @abstractmethod
    def validate_rating(self,rating:float):
        pass

    @abstractmethod
    def validate_review(self,review:str):
        pass
    
    @abstractmethod
    def validate_customer_id_exists(self,customer_id:int):
        pass
    
    @abstractmethod
    def validate_product_id_exists(self,product_id:int):
        pass

    @abstractmethod
    def validate_feedback_id_exists(self,feedback_id:int):
        pass

    @abstractmethod
    def delete_feedback(self,feedback_id:int)->str:
        pass

    @abstractmethod
    def get_feedbacks(self,limit:int,offset:int)->list[FeedbackDto]:
        pass

    @abstractmethod
    def update_feedback(self,feedback_id:int,rating:float,review:str)->FeedbackDto:
        pass

    @abstractmethod
    def validate_feedback_id(self,feedback_id:int):
        pass

    @abstractmethod
    def validate_order_id(self,order_id:int):
        pass

    @abstractmethod
    def validate_order_id_exists(self,order_id:int):
        pass

    @abstractmethod
    def cancel_order(self,order_id:int)->CancelOrderDto:
        pass

    @abstractmethod
    def update_order_status(self,order_id:int,status:str)->OrderStatusDto:
        pass

    @abstractmethod
    def validate_order_status(self,status:str):
        pass

    @abstractmethod
    def get_orders_list(self,limit:int,offset:int)->list[OrderDto]:
        pass

    @abstractmethod
    def search_orders(self,name:str,status:str):
        pass