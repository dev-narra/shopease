from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomePhone,InvalidCustomerAddress,InvalidCustomerEmail,InvalidCustomerName,InvalidEmail,CustomerAlreadyExist

class CreateCustomerInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def create_customer(self,name:str,email:str,phone:str,address:str,presenter:PresenterInterface):

        try:
            self.storage.validate_customer(email=email)
        except CustomerAlreadyExist:
            return presenter.raise_exception_for_customer_alredy_exists()

        valid_input_data=self.validate_input_data(name=name,email=name,phone=phone,address=phone,presenter=presenter)
        if valid_input_data:
            return valid_input_data

        customer_id=self.storage.create_customer(name=name,email=email,phone=phone,address=address)
        return presenter.get_response_for_create_customer(customer_id)



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