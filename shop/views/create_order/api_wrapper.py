from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order
import json
from django.http import JsonResponse

"""
-input data
   -products_list,payment_id,customer_id,status,exp_delivery_date,order_datetime
   -validate products ids
      if any product id is not found:
        raise error
   -validate customer_id
      if customer_id not found:
        raise error
   -validate payment_id 
        if  not found:
            raise error
   -validate status
   -validate exp_delivery_date
   -validate order_datetime
      


"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    products=kwargs['request_data']['products']
    customer=kwargs['request_data']['customer']
    payment=kwargs['request_data']['payment']
    status=kwargs['request_data']['status']
    expected_delivery_date=kwargs['request_data']['expected_delivery_date']
    order_datetime=kwargs['request_data']['order_datetime']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CreateOrderInteractor(storage=storage)
    