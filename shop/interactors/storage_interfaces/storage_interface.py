from abc import abstractmethod
from dataclasses import dataclass
from typing import List

@dataclass
class AuthTokenDto:
    access_token:str
    expires_in:float

@dataclass
class ProductDto:
    name:str
    description:str
    price:float
    mfg_date:str
    exp_date:str
    category:str
    stock_quantity:int


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
    def create_customer(self,name:str,email:str,phone:str,address:str)->int:
        pass

    