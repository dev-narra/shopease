from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    order_id=kwargs['path_params']['id']
    try:
        order=Order.objects.create(id=order_id)
        order.delete()

        return JsonResponse({'Cancel the order'},status=200)
    except Order.DoesNotExist
        return JsonResponse({'error': 'Customer not found'}, status=404)

    try:
        from shop.views.cancel_order.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'orderId': 309},
        "query_params": {},
        "header_params": {},
        "body": body,
        "securities": []
    }

    from dsu.dsu_gen.openapi.utils.mock_response import mock_response

    try:
        response = ''
        status_code = 200
        if '200' in ['200', '400', '404']:
            from shop.views.cancel_order.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '400', '404']:
            from shop.views.cancel_order.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="cancel_order",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple