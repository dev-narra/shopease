from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidPaymentAmount,InvalidPaymentMethod,InvalidPaymentTransactionDate

class CreatePaymentInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage


    def create_payment(self,amount:float,method:str,transaction_date:str,presenter=PresenterInterface):

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

        payment_id=self.storage.create_payment(amount=amount,payment=payment,transaction_date=transaction_date)
        return presenter.get_response_for_create_payment(product_id)
    