from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface

class GetProductsInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def get_products(self,limit:int,offset:int,presenter=PresenterInterface):
        products=self.storage.get_products(limit=limit,offset=offset)
        return presenter.get_response_for_get_products(products)