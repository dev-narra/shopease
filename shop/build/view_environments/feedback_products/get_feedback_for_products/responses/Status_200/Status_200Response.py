class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"rating": 1.1, "review": "string"}]',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.feedback_products.get_feedback_for_products.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass