from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.interactors.storage_interfaces.storage_interface import AuthTokenDto,ProductDto
from shop.constants.exception_messages import INVALID_EMAIL,INVALID_CUSTOMER_EMAIL,INVALID_CUSTOMER_PHONE,INVALID_CUSTOMER_ADDRESS,INVALID_CUSTOMER_NAME,CUSTOMER_ALREADY_EXISTS

from django_swagger_utils.drf_server.exceptions import NotFound
from typing import List

class PresenterImplementation(PresenterInterface):
    def raise_exception_for_invalid_email(self):
        NotFound(*INVALID_EMAIL)

    def get_response_for_user_login(self,auth_tokens:AuthTokenDto):
        return{
            "access_token":auth_tokens.access_token,
            "expires_in":auth_tokens.expires_in
        }
    
    def get_response_for_get_products(self,products:List[ProductDto]):
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

    def get_response_for_search_products(self,products:List[ProductDto]):
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
        NotFound(*INVALID_CUSTOMER_EMAIL)

    def raise_exception_for_invalid_customer_phone(self):
        NotFound(*INVALID_CUSTOMER_PHONE)

    def raise_exception_for_invalid_customer_address(self):
        NotFound(*INVALID_CUSTOMER_ADDRESS)

    def raise_exception_for_invalid_customer_name(self):
        NotFound(*INVALID_CUSTOMER_NAME)

    def raise_exception_for_customer_alredy_exists(self):
        NotFound(*CUSTOMER_ALREADY_EXISTS)

    def raise_exception_for_customer_input_data(self):
        NotFound()