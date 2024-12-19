class Status200Response(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"name": "string", "description": "string", "price": 1.1, "mfg_date": "string", "exp_date": "string", "category": "string", "stock_quantity": 1.1, "product_id": 1}',
            "response_serializer": "ProductSerializer",
            "response_serializer_import_str": "from shop.build.serializers.definitions.Product.ProductSerializer import ProductSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass