path_method_dict = {
    "product/create/": {
        "POST": "create_product"
    }
}


def product_create_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "product_create_", operations_dict, request, *args, **kwargs)
    return response