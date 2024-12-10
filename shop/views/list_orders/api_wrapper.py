from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    limit=kwargs['query_params']['limit']
    offset=kwargs['query_params']['offset']
    orders=Order.objects.all()[offset:offset+limit]
    orders_array=[]
    for order in orders:
        data={'customer':order.customer,'products':order.products,'payment':order.payment,'status':order.status,'order_datetime'=order.order_datetime,'exp_delivery_date'=order.exp_delivery_date}
        orders_array.append(data)
    return JsonResponse(orders_array,safe=False,status=200)

    try:
        from shop.views.list_orders.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {},
        "query_params": {'page': 447, 'size': 137},
        "header_params": {},
        "body": body,
        "securities": []
    }

    from dsu.dsu_gen.openapi.utils.mock_response import mock_response

    try:
        response = ''
        status_code = 200
        if '200' in ['200']:
            from shop.views.list_orders.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.list_orders.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="list_orders",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple