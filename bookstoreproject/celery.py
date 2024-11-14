import os
from celery import Celery
from django.conf import settings

# set settings for celery cmd program
os.environ.setdefault('DJANGO-SETTINGS-MODULE', 'bookstoreproject.settings')

app = Celery('bookstoreproject', broker=settings.CELERY_BROKER_URL)

# automatically discover tasks given in different apps
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.update(
    result_backend='django-db',
)

