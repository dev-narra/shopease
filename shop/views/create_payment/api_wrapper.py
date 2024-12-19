from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.create_payment_interactor import CreatePaymentInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Payment
from django.http import HttpResponse
import json

"""
-inputs:
    -amount, method, transaction_date
-validate the inputs
    -if any input is None
       raise exception
    else
       create a payment

"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs.get('request_data', {})
    amount=request_data.get('amount')
    method=request_data.get('method')
    transaction_date=request_data.get('transaction_date')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CreatePaymentInteractor(storage=storage)
    
    payment_id=interactor.create_payment(amount=amount,method=method,transaction_date=transaction_date,presenter=presenter)
    response_data=json.dumps(payment_id)
    return HttpResponse(response_data,status=201)



    