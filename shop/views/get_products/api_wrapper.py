from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_products_interactor import GetProductsInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import HttpResponse
import json


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetProductsInteractor(storage=storage)

    products_list=interactor.get_products(limit=limit,offset=offset,presenter=presenter)
    response_data=json.dumps(products_list)

    return HttpResponse(response_data,status=201)


    