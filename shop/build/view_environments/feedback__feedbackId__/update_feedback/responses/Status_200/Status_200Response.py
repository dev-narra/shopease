class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"rating": 1.1, "review": "string"}',
            "response_serializer": "FeedbackSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.Feedback.FeedbackSerializer import FeedbackSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass