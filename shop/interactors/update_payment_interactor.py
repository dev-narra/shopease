from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidPaymentAmount,InvalidPaymentMethod,InvalidPaymentTransactionDate,InvalidPaymentId

class UpdatePatamentInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def update_payment(self,payment_id:int,amount:float,method:str,transaction_date:str,presenter:PresenterInterface):
         
        self.validate_input_data(amount=amount,method=method,transaction_date=transaction_date,presenter=presenter)
        
        
        try:
            self.storage.validate_payment_id(payment_id=payment_id)
        except InvalidPaymentId:
            presenter.raise_exception_for_invalid_payment_id()

        payment=self.storage.update_payment(payment_id=payment_id,amount=amount,method=method,transaction_date=transaction_date)
        return presenter.get_response_for_update_payment(payment)
            
        
    def validate_input_data(self,amount:float,method:str,transaction_date:str,presenter:PresenterInterface):

        try:
            self.storage.validate_payment_amount(amount=amount)
        except InvalidPaymentAmount:
            presenter.raise_exception_for_invalid_payment_amount()

        try:
            self.storage.validate_payment_method(method=method)
        except InvalidPaymentMethod:
            presenter.raise_exception_for_invalid_payment_method()

        try:
            self.storage.validate_payment_transaction_date(transaction_date=transaction_date)
        except InvalidPaymentTransactionDate:
            presenter.raise_exception_for_invalid_payment_transaction_date()
        
        return None