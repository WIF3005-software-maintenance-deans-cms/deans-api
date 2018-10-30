from django_cron import CronJobBase, Schedule
from models import Crisis
import logging
logger = logging.getLogger("django")

import time
import requests

class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 1
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'    # a unique code

    def do(self):
        url = "http://notification:8000/"
        headers = {
            'Content-Type': "application/json",
            }
        response = requests.request("GET", url, headers=headers)

        logger.info(response.text)

        logger.info('Sent email to President Office.')
        time.sleep(10)