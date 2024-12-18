from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.create_product_interactor import CreateProductInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import  HttpResponse
import json

"""
Inputs:
       name,description,price,mfg_date,exp_date,category,stock_quantity
Validate input_fields:
       -validate name,description.......
       if any input is None:
          raise InvalidInput
       else
          if product name not in db:
            create product 
          else
            raise InvalidProductName


"""




@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs.get('request_data', {})
    name=request_data.get('name')
    description=request_data.get('description')
    price=request_data.get('price')
    mfg_date=request_data.get('mfg_date')
    exp_date=request_data.get('exp_date')
    category=request_data.get('category')
    stock_quantity=request_data.get('stock_quantity')

    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=CreateProductInteractor(storage=storage)

    product_id=interactor.create_product(name=name,description=description,price=price,mfg_date=mfg_date,exp_date=exp_date,category=category,stock_quantity=stock_quantity,presenter=presenter)

    response_data=json.dumps(product_id)

    return HttpResponse(response_data,status=201)

    

