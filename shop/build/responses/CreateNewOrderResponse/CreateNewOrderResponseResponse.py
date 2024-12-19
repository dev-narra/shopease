class CreateNewOrderResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": "string", "products": [{"name": "string", "description": "string", "price": 1.1, "mfg_date": "string", "exp_date": "string", "category": "string", "stock_quantity": 1.1, "id": 1}], "customer": {"id": 1, "name": "string", "email": "string", "phone": "string", "address": "string"}, "payment": {"id": 1, "amount": 1.1, "method": "Card", "transaction_date": "string"}, "status": "Pending", "expected_delivery_date": "2099-12-31", "order_datetime": "2099-12-31 00:00:00"}',
            "response_serializer": "OrderSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.Order.OrderSerializer import OrderSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass