from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_customers_interactor import GetCustomersInteractor


from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Customer
import json
from django.http import HttpResponse

"""
  - get the limit and offset
      - validate limit
      - validate offset
  - storage impl
     - get_customer

  - presenter implement 
      - get_response_for_gets_the_customers



"""



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetCustomersInteractor(storage=storage)
    customers=interactor.get_customers(limit=limit,offset=offset,presenter=presenter)
    response_data=json.dumps(customers)
    return HttpResponse(response_data,status=200)
