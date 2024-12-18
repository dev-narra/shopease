from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Customer
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs.get('request_data', {})
    name=request_data.get('name')
    email=request_data.get('email')
    phone=request_data.get('phone')
    address=request_data.get('address')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CreateCustomerInteractor(storage=storage)
    
    customer_id=interactor.create_customer(name=name,email=email,phone=phone,address=address)
    response_data=json.dumps(customer_id)

    return HttpResponse(response_data,status=201)
    