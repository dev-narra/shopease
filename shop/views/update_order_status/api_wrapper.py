from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.update_order_status_interactor import UpdateOrderStatusInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-input: order_id,status
-validate the inputs
   - validate order_id 
       if order_id is None
         raise error Invalid order_id
       else
          verify the order_id exists 
             if not raise error
             else do updation

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    order_id=kwargs['path_params']['orderId']
    status=kwargs['request_data']['status']
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=UpdateOrderStatusInteractor(storage=storage)
    order=interactor.update_order_status(order_id=order_id,status=status,presenter=presenter)
    response_data=json.dumps(order)
    return HttpResponse(response_data,status=200)
