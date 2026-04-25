import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJNAGO_SETTINGS_MODULE', 'djangoproject.settings')

application = get_asgi_application()