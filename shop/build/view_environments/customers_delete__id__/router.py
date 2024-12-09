path_method_dict = {
    "customers/delete/(?P<id>[-\\w]+)/": {
        "DELETE": "delete_customer"
    }
}


def customers_delete__id__(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "customers_delete__id__", operations_dict, request, *args, **kwargs)
    return response