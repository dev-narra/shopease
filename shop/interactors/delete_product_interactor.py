from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidProductId

class DeleteProductInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=StorageInterface

    def delete_product(self,id:int,presenter:PresenterInterface):
        
        try:
            self.storage.validate_product_id(id=id)
        except InvalidProductId:
            presenter.raise_exception_for_invalid_product_id()

        self.storage.delete_product(self,id=id)
        return presenter.get_response_for_delete_product()