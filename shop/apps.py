from django.apps import AppConfig

class ShopAppConfig(AppConfig):
    name = "shop"

    def ready(self):
        from shop import signals # pylint: disable=unused-variable
