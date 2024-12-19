class Status400Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"error": "string"}',
            "response_serializer": "Status_400Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.payments__id_.update_payment_details.responses.Status_400.Status_400.Status_400Serializer import Status_400Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass