from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Order
import json
from django.http import JsonResponse

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    customer=kwargs['customer']
    products=kwargs['products']
    payment=kwargs['payment']
    request_data=kwargs['request_data']
    status=request_data.get('status')
    exp_delivery_date=request_data.get('exp_delivery_date')
    order_datetime=request_data.get('order_datetime')

    order=Order.objects.create(
        products=products,customer=customer,payment=payment,status=status,exp_delivery_date=exp_delivery_date,order_datetime=order_datetime
    )

    data = json.dumps({'order_id': order.id})
    response = HttpResponse(data, status=201)
    return response

    try:
        from shop.views.create_order.request_response_mocks \
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
            from shop.views.create_order.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.create_order.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="create_order",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple