from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomerName

class GetOrdersListInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def search_orders(self,name:str,status:str,presenter:PresenterInterface):

        try:
            self.storage.validate_customer_name(name=name)
        except InvalidCustomerName:
            presenter.raise_exception_for_invalid_customer_name()

        orders=self.storage.search_orders(name=name,status=status)
        return presenter.get_response_for_search_orders(orders)