from django_cron import CronJobBase, Schedule
from .models import Crisis, SiteSettings
import datetime
import requests

import logging
logger = logging.getLogger("django")


class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 1
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'    # a unique code

    @classmethod
    def construct_report_data(self):
        payload = {}
        {"email": "xinyesg@gmail.com", "cases": [
            {"time": "now", "location": "JP", "type": "fire", "status": "Dispatched", "resolved_in": 9.9}]}
        
        created_time = datetime.datetime.now() - datetime.timedelta(minutes=30)

        latest_crisis = Crisis.objects.filter(crisis_time__gte=created_time)

        payload['email'] = SiteSettings.load().summary_reporting_email
        payload['cases'] = [ 
            {
                "time":i.crisis_time, 
                "location": i.crisis_location1 + "\n" + i.crisis_location2,
                "type": [j.name for j in i.crisis_type.all()],
                "status": i.crisis_status,
                "resolved_in": i.updated_at if i.crisis_status == "RS" else "None"
            } for i in latest_crisis
            ]
        return latest_crisis

    def do(self):
        url = "http://notification:8000/reports/"
        payload = CronEmail.construct_report_data()
        headers = {
            'Content-Type': "application/json",
            'cache-control': "no-cache",
            'Postman-Token': "39233191-7871-4784-b54d-d4f89e03032e"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)

        logger.info(response.text)

        logger.info('Sent email to President Office.')
