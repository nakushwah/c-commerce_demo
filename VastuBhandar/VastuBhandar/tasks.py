from celery.utils.log import get_task_logger
from time import sleep
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return 'first_task_done'


my_first_task.delay(10)
