from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomePhone,InvalidCustomerAddress,InvalidCustomerEmail,InvalidCustomerName,InvalidEmail,CustomerAlreadyExist

class CreateCustomerInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def create_customer(self,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):
        
        self.validate_input_data(name=name,email=name,phone=phone,address=phone,presenter=presenter)
        
        try:
            self.storage.validate_customer(email=email)
        except CustomerAlreadyExist:
            presenter.raise_exception_for_customer_alredy_exists()


        customer_id = self.storage.create_customer(name=name,email=email,phone=phone,address=address)
        return presenter.get_response_for_create_customer(customer_id)



    def validate_input_data(self,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):
        try:
            self.storage.validate_customer_name(name=name)
        except InvalidCustomerName:
            presenter.raise_exception_for_invalid_customer_name()

        try:
            self.storage.validate_customer_email(email=email)
        except InvalidCustomerEmail:
            presenter.raise_exception_for_invalid_customer_email()

        try:
            self.storage.validate_customer_phone(phone=phone)
        except InvalidCustomePhone:
            presenter.raise_exception_for_invalid_customer_phone()

        try:
            self.storage.validate_customer_address(address=address)
        except InvalidCustomerAddress:
            presenter.raise_exception_for_invalid_customer_address()
            
        return none