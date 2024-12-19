from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_payments_interactor import GetPaymentsInteractor
from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Payment
from django.http import HttpResponse
import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetPaymentsInteractor(storage=storage)
    payments_array=interactor.get_payments(limit=limit,offset=offset,presenter=presenter)
    response_data=json.dumps(payments_array)
    return HttpResponse(response_data)
    