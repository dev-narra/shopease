class CreateNewCustomerResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"id": "string", "name": "string", "email": "string", "phone": "string", "address": "string", "createdOn": "string", "ProductId": "string"}',
            "response_serializer": "CustomerWithExtraFieldsSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.CustomerWithExtraFields.CustomerWithExtraFieldsSerializer import CustomerWithExtraFieldsSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass