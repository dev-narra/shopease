from shop.storages.storages_implementation import StorageImplementation
from shop.presenters.presenters_implementation import PresenterImplementation
from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
import json
from django.db.models import Q

"""
-get query_params
-storage impl
   -search_products
     - if name or category contains products
            return products
-presenter impl 
   - get_response_for_search_products

-interactor 
   - SearchProductIntreactor

"""

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    name=kwargs['query_params']['name']
    category=kwargs['query_params']['category']
    
    storage=StorageImplementation()
    presenter=PresenterImplementation()

    interactor=SearchProductIntreactor(storage=storage)
    products=interactor.search_products(name=name,category=name)

    response_data=json.dumps(products)
    return HttpResponse(response_data,status=201)