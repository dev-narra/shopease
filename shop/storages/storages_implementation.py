from shop.interactors.storage_interfaces.storage_interface import StorageInterface,AuthTokenDto,ProductDto
from ib_users.interfaces.service_interface import ServiceInterface
from shop.models import User,Product,Customer
from typing import List



class StorageImplementation(StorageInterface):
       def validate_email(self,email:str):
         is_valid_email=Use.objects.filter(email=email).exists()
         is_invalid_email=not is_valid_email
         if is_invalid_email:
            raise InvalidEmail
       
       def user_login(self,email:str)->AuthTokenDto:
          user = User.objects.get(email=email).id
          service_interface = ServiceInterface()
          auth_tokens = service_interface.create_auth_tokens_for_user(user)
          return auth_tokens
      
       def get_products(self,limit:int,offset:int)->List[ProductDto]:
          products=Product.objects.all()[offset:offset+limit]
          return products

       def create_customer(self,name:str,email:str,phone:str,address:str)->int:
          customer=Customer.objects.create(name=name,email=email,phone=phone,address=address)
          customer_id=customer.id
          return customer_id