path_method_dict = {
    "product/update/(?P<id>\\d+)/": {
        "PUT": "update_product"
    }
}


def product_update__id__(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "product_update__id__", operations_dict, request, *args, **kwargs)
    return response