from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.search_customers_interactor import SearchCustomerIntreactor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-Search customers based on name or email
-get the query_params
      -name
      -email
-validate the name and email
    if name or email exists:
        return the customers
    else:
        return none

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    name=kwargs['query_params']['name']
    email=kwargs['query_params']['email']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=SearchCustomerIntreactor(storage=storage)
    customers=interactor.search_customers(name=name,email=email,presenter=presenter)
    response_data=json.dumps(customers)
    return HttpResponse(response_data,status=200)
