from django.conf.urls import include
from django.urls import re_path

from shop.build.view_environments.todos_.router import todos_
from shop.build.view_environments.todos__id__.router import todos__id__


base_path = "api/shop/"

api_paths = [
    re_path(r'^todos/$', todos_),
    re_path(r'^todos/(?P<id>\d+)/$', todos__id__),
]


urlpatterns = [
    re_path(r'^{base_path}'.format(base_path=base_path), include(api_paths))
]
