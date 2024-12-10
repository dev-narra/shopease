from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Product
from django.http import JsonResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    request_data = kwargs.get('request_data', {})
    name=request_data.get('name')
    description=request_data.get('description')
    price=request_data.get('price')
    mfg_date=request_data.get('mfg_date')
    exp_date=request_data.get('exp_date')
    category=request_data.get('category')
    stock_quantity=request_data.get('stock_quantity')

    product=Product.objects.create(
        name=name,
        description=description,
        price=price,
        mfg_date=mfg_date,
        exp_date=exp_date,
        category=category,
        stock_quantity=stock_quantity
    )

    response_data = {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "mfg_date": product.mfg_date,
            "exp_date": product.exp_date,
            "category": product.category,
            "stock_quantity": product.stock_quantity,
        }
    return JsonResponse(response_data, status=201)


    try:
        from shop.views.create_product.request_response_mocks \
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
        if '200' in ['200']:
            from shop.views.create_product.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.create_product.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="create_product",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple