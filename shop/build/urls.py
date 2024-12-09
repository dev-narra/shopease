from django.urls import re_path

from shop.build.view_environments.auth_login_.router import auth_login_
from shop.build.view_environments.products_.router import products_
from shop.build.view_environments.products_search_.router import products_search_
from shop.build.view_environments.product_create_.router import product_create_
from shop.build.view_environments.product_update__id__.router import product_update__id__
from shop.build.view_environments.product_delete__id__.router import product_delete__id__
from shop.build.view_environments.products_low_stock_.router import products_low_stock_
from shop.build.view_environments.customers_.router import customers_
from shop.build.view_environments.customer_create_.router import customer_create_
from shop.build.view_environments.customers_update__id__.router import customers_update__id__
from shop.build.view_environments.customers_delete__id__.router import customers_delete__id__
from shop.build.view_environments.customers_search_.router import customers_search_
from shop.build.view_environments.orders_.router import orders_
from shop.build.view_environments.orders_search_.router import orders_search_
from shop.build.view_environments.order_create_.router import order_create_
from shop.build.view_environments.orders__orderId__status_.router import orders__orderId__status_
from shop.build.view_environments.orders__orderId__cancel_.router import orders__orderId__cancel_
from shop.build.view_environments.payments_.router import payments_
from shop.build.view_environments.payments_search_.router import payments_search_
from shop.build.view_environments.payment_create_.router import payment_create_
from shop.build.view_environments.payments__paymentId_.router import payments__paymentId_
from shop.build.view_environments.feedback_products.router import feedback_products
from shop.build.view_environments.product__productId__feedback_.router import product__productId__feedback_
from shop.build.view_environments.feedback__feedbackId__.router import feedback__feedbackId__
from shop.build.view_environments.feedback_delete__feedbackId__.router import feedback_delete__feedbackId__


urlpatterns = [
    re_path(r'^auth/login/$', auth_login_),
    re_path(r'^products/$', products_),
    re_path(r'^products/search/$', products_search_),
    re_path(r'^product/create/$', product_create_),
    re_path(r'^product/update/(?P<id>\d+)/$', product_update__id__),
    re_path(r'^product/delete/(?P<id>[-\w]+)/$', product_delete__id__),
    re_path(r'^products/low/stock/$', products_low_stock_),
    re_path(r'^customers/$', customers_),
    re_path(r'^customer/create/$', customer_create_),
    re_path(r'^customers/update/(?P<id>[-\w]+)/$', customers_update__id__),
    re_path(r'^customers/delete/(?P<id>[-\w]+)/$', customers_delete__id__),
    re_path(r'^customers/search/$', customers_search_),
    re_path(r'^orders/$', orders_),
    re_path(r'^orders/search/$', orders_search_),
    re_path(r'^order/create/$', order_create_),
    re_path(r'^orders/(?P<orderId>\d+)/status/$', orders__orderId__status_),
    re_path(r'^orders/(?P<orderId>\d+)/cancel/$', orders__orderId__cancel_),
    re_path(r'^payments/$', payments_),
    re_path(r'^payments/search/$', payments_search_),
    re_path(r'^payment/create/$', payment_create_),
    re_path(r'^payments/(?P<paymentId>\d+)/$', payments__paymentId_),
    re_path(r'^feedback/products/$', feedback_products),
    re_path(r'^product/(?P<productId>\d+)/feedback/$', product__productId__feedback_),
    re_path(r'^feedback/(?P<feedbackId>\d+)/$', feedback__feedbackId__),
    re_path(r'^feedback/delete/(?P<feedbackId>\d+)/$', feedback_delete__feedbackId__),
]