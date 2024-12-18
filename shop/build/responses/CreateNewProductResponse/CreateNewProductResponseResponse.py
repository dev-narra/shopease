class CreateNewProductResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"product_id": 1}',
            "response_serializer": "CreateNewProductResponseSerializer",
            "response_serializer_import_str": "from shop.build.responses.CreateNewProductResponse.CreateNewProductResponse.CreateNewProductResponseSerializer import CreateNewProductResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass