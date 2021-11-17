"""
    configure the celery for creating and sharing the task
    using celery package
"""


from __future__ import absolute_import
from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VastuBhandar.settings')
app = Celery('VastuBhandar')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)




