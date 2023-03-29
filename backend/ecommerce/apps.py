from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'

    # connects to the signals.py when the app starts
    def ready(self):
        import ecommerce.signals
