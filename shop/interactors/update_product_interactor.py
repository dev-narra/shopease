from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidProductName,InvalidDescription,InvalidPrice,InvalidMfgDate,InvalidExpDate,InvalidCategory,InvalidStockQuantity

class UpdateProductInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage