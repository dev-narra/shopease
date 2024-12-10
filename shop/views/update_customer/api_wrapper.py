from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from shop.models import Customer
from django.http import JsonResponse


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    path_params = kwargs.get('path_params')
    if not path_params:
        return JsonResponse({'error': 'Path parameters are missing'}, status=400)

    customer_id = path_params.get('id')
    if not customer_id:
        return JsonResponse({'error': 'customer ID is missing'}, status=400)

    request_data = kwargs.get('request_data', {})
    try:
        name=request_data.get('name'),
        email=request_data.get('email'),
        phone=request_data.get('phone'),
        address=request_data.get('address')

        customer=Customer.objects.get(id=customer_id)
        customer.name=name
        customer.email=email
        customer.phone=phone
        customer.address=address
        customer.save()

        response_data={
            "id":customer.id,
            "name":customer.name,
            "email":customer.email,
            "phone":customer.phone,
            "address":customer.address
        }

        return JsonResponse(response_data,status=200)
    except Customer.DoesNotExist:
        return JsonResponse({'error': 'Customer not found'}, status=404)


    try:
        from shop.views.update_customer.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'id': 'string'},
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
            from shop.views.update_customer.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.update_customer.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="update_customer",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple