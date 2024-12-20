from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidProductName,InvalidCategory

class SearchProductIntreactor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def search_products(self,name:str,category:str,presenter:PresenterInterface):
        
        try:
            self.storage.validate_product_name(name=name)
        except InvalidProductName:
            presenter.raise_exception_for_invalid_product_name()

        try:
            self.storage.validate_category(category=category)
        except InvalidCategory:
            presenter.raise_exception_for_invalid_category()

        products=self.storage.search_products(name=name,category=name)
        return presenter.get_response_for_search_products(products)