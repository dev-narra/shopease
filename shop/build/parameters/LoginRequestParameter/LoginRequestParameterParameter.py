class LoginParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "LoginRequestParameter",
            "parameter_field_name": "login"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "LoginRequestSerializer",
            "param_serializer_import_str": "from shop.build.serializers.definitions.LoginRequest.LoginRequestSerializer import LoginRequestSerializer",
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