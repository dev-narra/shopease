class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"message": "string", "orderId": 1, "status": "string", "inventoryUpdated": true}',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.orders__orderId__cancel_.cancel_order.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass