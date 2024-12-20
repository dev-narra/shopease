from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import OrderIdDoesNotExist,InvalidOrderId,InvalidOrderStatus

class UpdateOrderStatusInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage
    
    def update_order_status(self,order_id:int,status:str,presenter=PresenterInterface):

        valid_input_data=validate_input_data(self,order_id=order_id,status=status,presenter=presenter)
        if valid_input_data:
            return valid_input_data

        try:
            self.storage.validate_order_id_exists(order_id=order_id)
        except OrderIdDoesNotExist:
            presenter.raise_exception_for_order_id_not_exists()

        order=self.storage.update_order_status(order_id=order_id,status=status)
        return presenter.get_response_for_update_order_status(order)
    
    def validate_input_data(self,order_id:int,status:str,presenter:PresenterInterface):
           
        try:
            self.storage.validate_order_status(status=status)
        except InvalidOrderStatus:
            presenter.raise_exception_for_invalid_order_status()

        try:
            self.storage.validate_order_id(order_id=order_id)
        except InvalidOrderId:
            presenter.raise_exception_for_invalid_order_id()

        return None