from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from shop.models import Product

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']
    products=Product.objects.all()[offset:offset+limit]
    products_array=[]
    for product in products:
        data={'name':product.name,'description':product.description,'price':product.price,'mfg_date':product.mfg_date,'exp_date':product.exp_date,'category':product.category,'stock_quantity':product.stock_quantity}
        products_array.append(data)
    return JsonResponse(products_array,safe=False,status=200)



    try:
        from shop.views.get_products.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "body": body,
        "securities": []
    }

    from dsu.dsu_gen.openapi.utils.mock_response import mock_response

    try:
        response = ''
        status_code = 200
        if '200' in ['200', '401', '403', '404']:
            from shop.views.get_products.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '401', '403', '404']:
            from shop.views.get_products.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="get_products",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple