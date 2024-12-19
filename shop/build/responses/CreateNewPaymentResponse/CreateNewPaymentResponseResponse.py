class CreateNewPaymentResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"customer_id": 1}',
            "response_serializer": "CreateNewPaymentResponseSerializer",
            "response_serializer_import_str": "from shop.build.responses.CreateNewPaymentResponse.CreateNewPaymentResponse.CreateNewPaymentResponseSerializer import CreateNewPaymentResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass