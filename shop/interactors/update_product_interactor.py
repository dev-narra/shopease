from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidProductName,InvalidDescription,InvalidPrice,InvalidMfgDate,InvalidExpDate,InvalidCategory,InvalidStockQuantity,InvalidProductId

class UpdateProductInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage
    
    def update_product(self,product_id:int,name:str,description:str,price:float,mfg_date:str,exp_date:str,category:str,stock_quantity:int,presenter:PresenterInterface):

        self.validate_input_data(name=name,description=name,price=price,mfg_date=mfg_date,exp_date=exp_date,category=category,stock_quantity=stock_quantity,presenter=presenter)

        try:
            self.storage.validate_product_id(product_id=product_id)
        except InvalidProductId:
            presenter.raise_exception_for_invalid_product_id()

        product=self.storage.update_product(product_id=product_id,name=name,description=description,price=price,mfg_date=mfg_date,exp_date=exp_date,category=category,stock_quantity=stock_quantity)
        return presenter.get_response_for_update_product(product)


    def validate_input_data(self,name:str,description:str,price:float,mfg_date:str,exp_date:str,category:str,stock_quantity:int,presenter:PresenterInterface):
        try:
            self.storage.validate_product_name(name=name)
        except InvalidProductName:
            presenter.raise_exception_for_invalid_product_name()

        try:
            self.storage.validate_description(description=description)
        except InvalidDescription:
            presenter.raise_exception_for_invalid_description()

        try:
            self.storage.validate_price(price=price)
        except InvalidPrice:
            presenter.raise_exception_for_invalid_price()

        try:
            self.storage.validate_mfg_date(mfg_date=mfg_date)
        except InvalidMfgDate:
            presenter.raise_exception_for_invalid_mfg_date()

        try:
            self.storage.validate_exp_date(exp_date=exp_date)
        except InvalidExpDate:
            presenter.raise_exception_for_invalid_exp_date()

        try:
            self.storage.validate_category(category=category)
        except InvalidCategory:
            presenter.raise_exception_for_invalid_category()

        try:
            self.storage.validate_stock_quantity(stock_quantity=stock_quantity)
        except InvalidStockQuantity:
            presenter.raise_exception_for_invalid_stock_quantity()

        return None
