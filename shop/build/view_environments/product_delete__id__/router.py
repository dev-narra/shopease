path_method_dict = {
    "product/delete/(?P<id>[-\\w]+)/": {
        "DELETE": "delete_product"
    }
}


def product_delete__id__(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "product_delete__id__", operations_dict, request, *args, **kwargs)
    return response