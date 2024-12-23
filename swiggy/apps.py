from django.apps import AppConfig


class SwiggyAppConfig(AppConfig):
    name = "swiggy"

    def ready(self):
        from swiggy import signals # pylint: disable=unused-variable
