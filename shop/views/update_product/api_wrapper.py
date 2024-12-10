from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from django.http import JsonResponse
from shop.models import Product

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    path_params = kwargs.get('path_params')
    if not path_params:
        return JsonResponse({'error': 'Path parameters are missing'}, status=400)

    product_id = path_params.get('id')
    if not product_id:
        return JsonResponse({'error': 'Product ID is missing'}, status=400)

    request_data = kwargs.get('request_data', {})
    try:
        name = request_data['name']
        description = request_data['description']
        price = float(request_data['price'])
        mfg_date = request_data['mfg_date']
        exp_date = request_data['exp_date']
        category = request_data['category']
        stock_quantity = float(request_data['stock_quantity'])
    except KeyError as e:
        return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)

    try:
        product = Product.objects.get(id=product_id)
        product.name = name
        product.description = description
        product.price = price
        product.mfg_date = mfg_date
        product.exp_date = exp_date
        product.category = category
        product.stock_quantity = stock_quantity
        product.save()

        response_data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'mfg_date': product.mfg_date,
            'exp_date': product.exp_date,
            'category': product.category,
            'stock_quantity': product.stock_quantity
        }
        return JsonResponse(response_data, status=200)

    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)

    try:
        from shop.views.update_product.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'id': 950},
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
            from shop.views.update_product.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.update_product.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="update_product",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple