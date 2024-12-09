class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": "string", "order_id": "string", "amount": 1.1, "method": "Card", "status": "Success", "transaction_date": "2099-12-31 00:00:00"}',
            "response_serializer": "PaymentSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.Payment.PaymentSerializer import PaymentSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass