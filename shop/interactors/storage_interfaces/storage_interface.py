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

class StorageInterface:

    @abstractmethod
    def validate_email(self,email:str):
        pass

    @abstractmethod
    def user_login(self,email:str)->AuthTokenDto:
        pass
   
    @abstractmethod
    def get_products(self,limit:int,offset:int)->List[ProductDto]:
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
    def update_customer(self,id:int,name:str,email:str,phone:str,address:str)->str:
        pass
    