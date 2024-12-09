class ProductParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CreateNewProductParameter",
            "parameter_field_name": "product"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "ProductSerializer",
            "param_serializer_import_str": "from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer",
            "param_serializer_required": False,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass