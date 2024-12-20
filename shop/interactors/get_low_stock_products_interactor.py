from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidStockValue

class GetLowStockProductsInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def get_low_stock_products(self,stock_value:int,presenter:PresenterInterface):

        try:
            self.storage.validate_stock_value(stock_value=stock_value)
        except InvalidStockValue:
            presenter.raise_exception_for_invalid_stock_value()

        products=self.storage.get_low_stock_products(stock_value=stock_value)
        return presenter.get_response_for_low_stock_products(products)

        