from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface

class SearchProductIntreactor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def search_products(self,name:str,category:str,presenter:PresenterInterface):

        

        products=self.storage.search_products(name=name,category=name)
        return presenter.get_response_for_search_products(products)