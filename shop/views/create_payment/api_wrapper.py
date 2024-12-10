from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Payment
from django.http import JsonResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    request_data = kwargs.get('request_data', {})
    amount=request_data.get('amount')
    method=request_data.get('method')
    transaction_date=request_data.get('transaction_date')

    payment=Payment.objects.create(
        amount=amount,
        method=method,
        transaction_date=transaction_date
    )

    response_data={
        "id":payment.id,
        "amount":payment.amount,
        "method":payment.method,
        "status":payment.status,
        "transaction_date":payment.transaction_date
    }
   
    return JsonResponse(response_data,status=201)


    try:
        from shop.views.create_payment.request_response_mocks \
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
        if '200' in ['200', '400']:
            from shop.views.create_payment.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '400']:
            from shop.views.create_payment.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="create_payment",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple