path_method_dict = {
    "products/search/": {
        "GET": "search_products"
    }
}


def products_search_(request, *args, **kwargs):
    from dsu.dsu_gen.openapi.utils.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from dsu.dsu_gen.openapi.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("shop", "products_search_", operations_dict, request, *args, **kwargs)
    return response