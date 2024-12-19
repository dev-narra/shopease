from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from shop.interactors.update_product_interactor import UpdateProductInteractor

from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import HttpResponse
from shop.models import Product
import json


"""
-inputs:
     -product_id, name, desctption......
-validate the input data
    - if any input data is none
       raise error
     else
        -vaidate the product_id
         if product_id exists:
            do updation
         else 
           raise Invalid productId

"""



@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs.get('path_params')
    product_id = path_params.get('id')
    request_data = kwargs.get('request_data', {})

    name = request_data['name']
    description = request_data['description']
    price = request_data['price']
    mfg_date = request_data['mfg_date']
    exp_date = request_data['exp_date']
    category = request_data['category']
    stock_quantity =request_data['stock_quantity']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()
    interactor=UpdateProductInteractor(storage=storage)
    product=interactor.update_product(product_id=product_id,name=name,description=description,price=price,mfg_date=mfg_date,exp_date=exp_date,category=category,stock_quantity=stock_quantity,presenter=presenter)
    response_data=json.dumps(product)
    return HttpResponse(response_data,status=200)
    