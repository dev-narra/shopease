from django.conf.urls import include
from django.urls import re_path

from shop.build.view_environments.products_.router import products_
from shop.build.view_environments.product_create_.router import product_create_


base_path = "api/shop/"

api_paths = [
    re_path(r'^products/$', products_),
    re_path(r'^product/create/$', product_create_),
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
