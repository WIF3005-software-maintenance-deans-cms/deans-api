from django_cron import CronJobBase, Schedule

import time

class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'    # a unique code


    def do(self):
        time.sleep(10)

