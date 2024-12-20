from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.cancel_order_interactor import CancelOrderInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order
import json
from django.http import HttpResponse


"""
-inputs: order_id
-validate the order_id
     if order id is none:
        raise error InvalidOrderId
     
     if order_id is exist:
        do cancel
     else 
       raise the error OrderIdDoesNotExist


"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    order_id=kwargs['path_params']['orderId']
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CancelOrderInteractor(storage=storage)
    order=interactor.cancel_order(order_id=order_id,presenter=presenter)
    response_data=json.dumps(order)
    return HttpResponse(response_data,status=200)
