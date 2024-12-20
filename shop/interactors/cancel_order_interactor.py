from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import OrderIdDoesNotExist,InvalidOrderId

class CancelOrderInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def cancel_order(self,order_id:int,presenter:PresenterInterface):

        try:
            self.storage.validate_order_id(order_id=order_id)
        except:
            presenter.raise_exception_for_invalid_order_id()

        try:
            self.storage.validate_order_id_exists(order_id=order_id)
        except:
            presenter.raise_exception_for_order_id_not_exists()

        order=self.storage.cancel_order(order_id=order_id)
        return presenter.get_response_for_cancel_order(order)