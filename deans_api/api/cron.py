from django_cron import CronJobBase, Schedule

class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'    # a unique code


    def do(self):
        pass    # do your thing here

