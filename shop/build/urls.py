from django.urls import re_path

from shop.build.view_environments.products_.router import products_
from shop.build.view_environments.product_create_.router import product_create_


urlpatterns = [
    re_path(r'^products/$', products_),
    re_path(r'^product/create/$', product_create_),
]