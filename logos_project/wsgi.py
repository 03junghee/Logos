import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logos_project.settings')

application = get_wsgi_application()
app = application  # 💡 이 줄을 추가하세요!