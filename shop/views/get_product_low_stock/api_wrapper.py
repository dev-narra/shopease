from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.get_low_stock_products_interactor import GetLowStockProductsInteractor


from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import HttpResponse
import json

"""
-inputs: stock_value
-validate the stock_value
    if stock_value is none
       raise error
    else
      based on the stock value, return the products which are below stock_value

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    stock_value=kwargs['query_params']['stock']
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=GetLowStockProductsInteractor(storage=storage)
    products_array=interactor.get_low_stock_products(stock_value=stock_value,presenter=presenter)
    response_data=json.dumps(products_array)
    return HttpResponse(response_data,status=200)

    