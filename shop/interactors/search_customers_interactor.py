from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomerEmail,InvalidCustomerName

class SearchCustomerIntreactor:

    def __init__(self,storage=StorageInterface):
        self.storage=StorageInterface

    def search_customers(self,name:str,email:str,presenter:PresenterInterface):

        try:
            self.storage.validate_customer_name(name=name)
        except InvalidCustomerName:
            presenter.raise_exception_for_invalid_customer_name()

        try:
            self.storage.validate_customer_email(email=email)
        except InvalidCustomerEmail:
            presenter.raise_exception_for_invalid_customer_email()

        customers=self.storage.search_customers(self,name=name,email=email)
        return presenter.get_response_for_search_customers(customers)
