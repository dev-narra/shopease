from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_orders_list_interactor import GetOrdersListInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order
import json
from django.http import HttpResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetOrdersListInteractor(storage=storage)
    orders_array=interactor.get_orders_list(limit=limit,offset=offset,presenter=presenter)
    response_data=json.dumps(orders_array)
    return HttpResponse(response_data)
    