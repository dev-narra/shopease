class LoginSuccessResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"token": "string", "user": {"id": 1, "email": "string@string.com", "role": "string"}}',
            "response_serializer": "LoginResponseSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.LoginResponse.LoginResponseSerializer import LoginResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass