from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.update_payment_interactor import UpdatePatamentInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
import json
from django.http import HttpResponse

"""
-inputs:
    -path_params
    -request_data
-validate the inputs
-validate the payment_id 
    if payment_is is exists:
        do updation
    else
      raise InvalidPaymentId


"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    payment_id=kwargs['path_params']['id']
    
    amount=kwargs['request_data']['amount']
    method=kwargs['request_data']['method']
    transaction_date=kwargs['request_data']['transaction_date']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=UpdatePatamentInteractor(storage=storage)
    payment=interactor.update_payment(payment_id=payment_id,amount=amount,method=method,transaction_date=transaction_date,presenter=presenter)
    response_data=json.dumps(payment)
    return HttpResponse(response_data,status=200)


