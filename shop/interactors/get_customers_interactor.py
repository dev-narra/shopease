from shop.interactors.storage_interfaces.storage_interface import StorageInterface
from shop.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from shop.exceptions.custom_exceptions import InvalidLimitValue,InvalidOffsetValue

class GetCustomersInteractor:

    def __init__(self,storage:StorageInterface):
        self.storage=storage

    def get_customers(self,limit:int,offset:int,presenter:PresenterInterface):

        try:
            self.storage.validate_limit_value(limit=limit)
        except InvalidLimitValue:
            presenter.raise_exception_for_invalid_limit_value()

        try:
            self.storage.validate_offset_value(offset=offset)
        except InvalidOffsetValue:
            presenter.raise_exception_for_invalid_offset_value()

        customers=self.storage.get_customers(limit=limit,offset=offset)
        return presenter.get_response_for_gets_the_customers(customers)