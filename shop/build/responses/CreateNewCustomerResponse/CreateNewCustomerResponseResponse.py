class CreateNewCustomerResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"customer_id": 1}',
            "response_serializer": "CreateNewCustomerResponseSerializer",
            "response_serializer_import_str": "from shop.build.responses.CreateNewCustomerResponse.CreateNewCustomerResponse.CreateNewCustomerResponseSerializer import CreateNewCustomerResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass