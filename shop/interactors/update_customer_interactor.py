from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomePhone,InvalidCustomerAddress,InvalidCustomerEmail,InvalidCustomerName,InvalidEmail,CustomerAlreadyExist

class UpdateCustomerInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def update_customer(self,id:int,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):

        self.validate_input_data(name=name,email=name,phone=phone,address=phone,presenter=presenter)

        try:
            self.storage.validate_customer_id(id=id)
        except InvalidCustomerId:
            presenter.raise_exception_for_invalid_customer_id()

        customer=self.storage.update_customer(id=id,name=name,email=email,phone=phone,address=address)
        return presenter.get_response_for_update_customer(customer)
    
    def validate_input_data(self,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):
        try:
            self.storage.validate_customer_name(name=name)
        except InvalidCustomerName:
            return presenter.raise_exception_for_invalid_customer_name()

        try:
            self.storage.validate_customer_email(email=email)
        except InvalidCustomerEmail:
            return presenter.raise_exception_for_invalid_customer_email()

        try:
            self.storage.validate_customer_phone(phone=phone)
        except InvalidCustomePhone:
            return presenter.raise_exception_for_invalid_customer_phone()

        try:
            self.storage.validate_customer_address(address=address)
        except InvalidCustomerAddress:
            return presenter.raise_exception_for_invalid_customer_address()
            
        return none