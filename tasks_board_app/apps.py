from django.apps import AppConfig


class TasksBoardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks_board_app'

    def ready(self):
        from .signals import create_auth_token
