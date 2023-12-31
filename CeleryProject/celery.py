from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryProject.settings')

app = Celery('CeleryProject')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Dhaka')
app.config_from_object(settings, namespace = 'CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule': crontab(hour=16, minute=45, day_of_month=24, month_of_year = 8),
        #'args': (2,)
    }

}

app.autodiscover_tasks()

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')