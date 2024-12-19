from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidCustomerId

class DeleteCustomerInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=StorageInterface

    def delete_customer(self,customer_id:int,presenter:PresenterInterface):

        try:
            self.storage.validate_customer_id(customer_id=customer_id)
        except InvalidCustomerId:
            presenter.raise_exception_for_invalid_customer_id()

        self.storage.delete_customer(customer_id=customer_id)
        return presenter.get_response_for_delete_customer()
