from django.apps import AppConfig


class ItemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.items'
    verbose_name = 'Items'

    def ready(self):
        import apps.items.signals
