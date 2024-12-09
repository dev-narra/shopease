class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"customers": [{"id": "string", "name": "string", "email": "string", "phone": "string", "address": "string"}], "total": 1, "page": 1, "size": 1}',
            "response_serializer": "CustomerListSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.CustomerList.CustomerListSerializer import CustomerListSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass