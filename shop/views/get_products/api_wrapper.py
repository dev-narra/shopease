from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.forms.models import model_to_dict

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs.get('query_params', {})

    if not request_data:
        request_data=kwargs.get('request_query_params', {})

    limit = int(request_data.get('limit', 5))  
    offset = int(request_data.get('offset', 0)) 

    products = Product.objects.all().order_by('id')

    paginator = Paginator(products, limit)  
    page_number = (offset // limit) + 1 
    paginated_products = paginator.get_page(page_number)

    products_list = [model_to_dict(product) for product in paginated_products]

    response_data = {
        "count": paginator.count,
        "next": f"?limit={limit}&offset={offset + limit}" if paginated_products.has_next() else None,
        "previous": f"?limit={limit}&offset={max(offset - limit, 0)}" if paginated_products.has_previous() else None,
        "results": products_list,
    }

    return JsonResponse(response_data, status=200)



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