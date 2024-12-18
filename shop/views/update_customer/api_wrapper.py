from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Customer
from django.http import HttpResponse
import json


"""
-input data: 
        customer_id,name,email,phone,address
-validate the input_data:

        if customer_id exist in db:
            perform update
        else
            raise InvalidCustomerId

 



"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs.get('path_params')

    id = path_params.get('id')
    request_data = kwargs.get('request_data', {})
    
    name=request_data.get('name'),
    email=request_data.get('email'),
    phone=request_data.get('phone'),
    address=request_data.get('address')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=UpdateProductInteractor(storage=storage)
    customer=interactor.update_customer(id=id,name=name,email=email,phone=phone,address=address)
    response_data=json.dumps(customer)

    return HttpResponse(response_data,status=201)