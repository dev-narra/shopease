from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass
from ib_users.interfaces.service_interface import ServiceInterface
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import IntegrityError
from shop.models import User
from django.core.exceptions import ObjectDoesNotExist


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    try:
        user_email = kwargs['request_data'].get('email')
        if not user_email:
            return JsonResponse({'error': 'User email parameter is missing'}, status=400)
        try:
            user = User.objects.get(email=user_email)
        except ObjectDoesNotExist:
            return JsonResponse({'error': f'User with email {user_email} does not exist'}, status=404)
        user = user.user_id
        service_interface = ServiceInterface()
        auth_tokens = service_interface.create_auth_tokens_for_user(user)
        data = {
            "access_token": auth_tokens.access_token,
            "expires_in": auth_tokens.expires_in
        }
        return Response(data, status=200)
    except IntegrityError as e:
        return JsonResponse({"error": "Database error occurred while processing the request"}, status=500)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)



    try:
        from shop.views.user_login.request_response_mocks \
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
        if '200' in ['200', '401', '400']:
            from shop.views.user_login.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '401', '400']:
            from shop.views.user_login.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="shop", test_case=test_case,
        operation_name="user_login",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple