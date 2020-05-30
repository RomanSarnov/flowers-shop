#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery.schedules import crontab
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowers_shop.settings')
celery_app = Celery('flowers_shop')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()



celery_app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-day': {
        'task': 'contact.tasks.send_newsletter',
        'schedule': crontab(),
    },
}