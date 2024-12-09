path_method_dict = {
    "orders/": {
        "GET": "list_orders"
    }
}


def orders_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "orders_", operations_dict, request, *args, **kwargs)
    return response