class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"message": "string"}',
            "response_serializer": "Status_200Serializer",
            "response_serializer_import_str": "from shop.build.view_environments.feedback_delete__feedbackId__.delete_feedback.responses.Status_200.Status_200.Status_200Serializer import Status_200Serializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass