from django.apps import AppConfig


class ProductsAppConfig(AppConfig):

    name = "tex_billd.products"
    verbose_name = "Products"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
