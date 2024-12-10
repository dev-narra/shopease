from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import JsonResponse
from django.db.models import Q

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    name_query=kwargs['query_params']['name']
    category_query=kwargs['query_params']['category']

    if name_query or category_query:
        products = Product.objects.filter(
            Q(name__icontains=name_query) | Q(category__icontains=category_query)
        )
    else:
        products = Product.objects.all()

    products_list = list(products.values()) 

    response_data = {
        "count": products.count(),
        "results": products_list,
    }

    return JsonResponse(response_data, status=200)

    
    try:
        from shop.views.search_products.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {},
        "query_params": {'name': 'string', 'category': 'string'},
        "header_params": {},
        "body": body,
        "securities": []
    }

    from dsu.dsu_gen.openapi.utils.mock_response import mock_response

    try:
        response = ''
        status_code = 200
        if '200' in ['200']:
            from shop.views.search_products.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.search_products.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="search_products",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple