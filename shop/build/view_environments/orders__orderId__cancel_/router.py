path_method_dict = {
    "orders/(?P<orderId>\\d+)/cancel/": {
        "PUT": "cancel_order"
    }
}


def orders__orderId__cancel_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "orders__orderId__cancel_", operations_dict, request, *args, **kwargs)
    return response