from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram_2024.accounts'

    def ready(self):
        import petstagram_2024.accounts.signals
