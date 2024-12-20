from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.search_payments_interactor import SearchPaymentsInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass

"""
-inputs:order_id 
-validate the input
  -validate orderId
  -check the order_id exists
     if not raise error

     

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
     order_id=kwargs['query_params']['orderId']
     customer_name=kwargs['query_params']['customerName']
     storage=StorageImplementation()
     presenter=PresenterImplementation()
     interactor=SearchPaymentsInteractor(storage=storage)