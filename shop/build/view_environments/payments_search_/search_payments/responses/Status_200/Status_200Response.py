class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"id": "string", "order_id": "string", "amount": 1.1, "method": "Card", "status": "Success", "transaction_date": "2099-12-31 00:00:00"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.payments_search_.search_payments.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass