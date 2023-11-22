from django.apps import AppConfig


class VmAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vm_app'
    
    def ready(self):
        import vm_app.views