from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.search_orders_interactor import SearchOrdersInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
inputs: name and status
-validate the inputs
   -validate name
   -validate status
   if any input is none
    raise error
   else
     return the orders which matches the name and status


"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    name=kwargs['query_params']['name']
    status=kwargs['query_params']['status']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=SearchOrdersInteractor(storage=storage)
    orders=interactor.search_products(name=name,status=status,presenter=presenter)
    response_data=json.dumps(orders)
    return HttpResponse(response_data,status=200)
    