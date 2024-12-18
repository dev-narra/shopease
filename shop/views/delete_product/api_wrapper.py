from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.delete_product_interactor import DeleteProductInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import HttpResponse
import json



"""
-validate the input
  -product_id

   if product_id in products:
        delete the product
   else
      raise InvalidProductId



"""


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    product_id = kwargs["path_params"]['id']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=DeleteProductInteractor(storage=storage)
    
    product_id=interactor.delete_product(id=id,presenter=presenter)
    response_data=json.dumps(product_id)

    return HttpResponse(response_data,status=200)
    

    
    