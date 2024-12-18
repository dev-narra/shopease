from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import JsonResponse
from django.db.models import Q

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    name_query=kwargs['query_params']['name']
    category_query=kwargs['query_params']['category']

    