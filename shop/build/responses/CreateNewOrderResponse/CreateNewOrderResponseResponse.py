class CreateNewOrderResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"order_id": 1}',
            "response_serializer": "CreateNewOrderResponseSerializer",
            "response_serializer_import_str": "from shop.build.responses.CreateNewOrderResponse.CreateNewOrderResponse.CreateNewOrderResponseSerializer import CreateNewOrderResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass