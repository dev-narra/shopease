class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": 1, "name": "string", "email": "string", "phone": "string", "address": "string"}',
            "response_serializer": "CustomerSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.Customer.CustomerSerializer import CustomerSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass