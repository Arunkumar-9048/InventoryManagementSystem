from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

class MyappConfig(AppConfig):
    name= 'myapp'
    
    def ready(self):
        from . scheduler import start_scheduler
        start_scheduler()