class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": 1}',
            "response_serializer": "ProductIdSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.ProductId.ProductIdSerializer import ProductIdSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass