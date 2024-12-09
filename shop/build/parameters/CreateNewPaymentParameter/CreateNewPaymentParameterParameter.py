class PaymentParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CreateNewPaymentParameter",
            "parameter_field_name": "payment"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "CreatePaymentRequestSerializer",
            "param_serializer_import_str": "from shop.build.serializers.definitions.CreatePaymentRequest.CreatePaymentRequestSerializer import CreatePaymentRequestSerializer",
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