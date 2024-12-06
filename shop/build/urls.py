from django.urls import re_path

from shop.build.view_environments.products_.router import products_
from shop.build.view_environments.product_create_.router import product_create_
from shop.build.view_environments.product_update__id_.router import product_update__id_
from shop.build.view_environments.product_delete__id_.router import product_delete__id_


urlpatterns = [
    re_path(r'^products/$', products_),
    re_path(r'^product/create/$', product_create_),
    re_path(r'^product/update/(?P<id>\d+)/$', product_update__id_),
    re_path(r'^product/delete/(?P<id>[-\w]+)/$', product_delete__id_),
]