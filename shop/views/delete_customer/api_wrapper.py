from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.delete_customer_interactor import DeleteCustomerInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Customer
from django.http import HttpResponse
import json

"""
-inputs:
    customer_id
    -validate customer_id 
     if customer_id exists()
       do deletion()
     else
       raise invalidCustomer

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    customer_id = kwargs["path_params"]['id']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=DeleteCustomerInteractor(storage=storage)
    customer=interactor.delete_customer(customer_id=customer_id,presenter=presenter)
    response_data=json.dumps(customer)
    return HttpResponse(response_data,status=200)