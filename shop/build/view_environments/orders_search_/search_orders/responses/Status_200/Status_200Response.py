class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"orders": [{"id": 1, "products": [{"product_id": 1}], "customer": {"customer_id": 1}, "payment": {"payment_id": 1}, "status": "Pending", "expected_delivery_date": "2099-12-31", "order_datetime": "2099-12-31"}]}',
            "response_serializer": "OrderListSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.OrderList.OrderListSerializer import OrderListSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass