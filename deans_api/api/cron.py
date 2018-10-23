from django_cron import CronJobBase, Schedule

import logging
logger = logging.getLogger(__name__)

import time


class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 0.5 # every 2 hours
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'    # a unique code

    def do(self):
        logger.info('Sent email to President Office.')
        time.sleep(10)