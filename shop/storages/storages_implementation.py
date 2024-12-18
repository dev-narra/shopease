from shop.interactors.storage_interfaces.storage_interface import StorageInterface,AuthTokenDto,ProductDto,CustomerDto
from ib_users.interfaces.service_interface import ServiceInterface
from shop.exceptions.custom_exceptions import InvalidCustomePhone,InvalidCustomerAddress,InvalidCustomerEmail,InvalidCustomerName,InvalidEmail,CustomerAlreadyExist
from shop.models import User,Product,Customer
from typing import List



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
      
       def get_products(self,limit:int,offset:int)->List[ProductDto]:
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
         is_valid_customer_id=Customer.objects.filter(id=id).exists()
         invalid_customer_id=not is_valid_customer_id
         if invalid_customer_id:
            raise InvalidCustomerId

       def create_customer(self,name:str,email:str,phone:str,address:str)->int:
          customer=Customer.objects.create(name=name,email=email,phone=phone,address=address)
          customer_id=customer.id
          return customer_id

       def search_products(self,name:str,category:str)->List[ProductDto]:
         if name or category:
            products = Product.objects.filter(
                Q(name__icontains=name) | Q(category__icontains=category)
            )
            return products
      
       def update_customer(self,id:int,name:str,email:str,phone:str,address:str):
         customer=Customer.objects.get(id=id)
         customer.id=id
         customer.name=name
         customer.email=email
         customer.phone=phone,
         customer.address=address
         customer.save()
         
         return customer
         


         