from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    user = kwargs['user']  
    request_data = kwargs['request_data']  
    name = request_data['name']
    email = request_data['email']
    phone = request_data['phone']
    address = request_data['address']


    customer = create_customer(
        user_id=user.id,
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    # Prepare the response data
    data = json.dumps({
        'customer_id': customer.id,
        'message': 'Customer created successfully'
    })
    response = HttpResponse(data, status=201, content_type='application/json')



    try:
        from shop.views.create_customer.request_response_mocks \
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
            from shop.views.create_customer.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200']:
            from shop.views.create_customer.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="create_customer",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple