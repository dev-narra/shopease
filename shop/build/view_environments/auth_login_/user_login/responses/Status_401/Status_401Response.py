class Status401Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"error": "string"}',
            "response_serializer": "Status_401Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.auth_login_.user_login.responses.Status_401.Status_401.Status_401Serializer import Status_401Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass