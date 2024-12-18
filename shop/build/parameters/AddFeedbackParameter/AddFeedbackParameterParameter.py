class FeedbackParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "AddFeedbackParameter",
            "parameter_field_name": "feedback"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "AddFeedbackRequestSerializer",
            "param_serializer_import_str": "from shop.build.serializers.definitions.AddFeedbackRequest.AddFeedbackRequestSerializer import AddFeedbackRequestSerializer",
            "param_serializer_required": True,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass