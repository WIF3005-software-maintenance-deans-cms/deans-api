from django_cron import CronJobBase, Schedule
from .models import Crisis, SiteSettings
import datetime
import requests
from django.template.loader import get_template
from django.template import Context

import logging
logger = logging.getLogger("django")

# email: {
#     "receiver": "aaa@gmail.com",
#     "content": "
#     <head> </head>
#     "
# }
# social_media
# {
#     "mesa": "
    
#     "
# }

email_template = get_template('president_email.html')


def construct_report_data():
    payload = {}

    d = Context({ 'username': username })
    html_content = htmly.render(d)

    
    created_time = datetime.datetime.now() - datetime.timedelta(minutes=30)
    latest_crisis = Crisis.objects.filter(crisis_time__gte=created_time)
    logger.info("Reporting" + str(len(latest_crisis))+ "crisis.")
    payload['email'] = SiteSettings.load().summary_reporting_email
    payload['cases'] = [ 
        {
            "crisis_time":i.crisis_time.strftime("%Y-%m-%d %H:%M:%S"), 
            "resolved_by": i.updated_at.strftime("%Y-%m-%d %H:%M:%S") if i.crisis_status == "RS" else "None",
            "location": i.crisis_location1 + "\n" + i.crisis_location2,
            "type": ", ".join([j.name for j in i.crisis_type.all()]),
            "status": i.crisis_status,
            "crisis_description": i.crisis_description,
            "crisis_assistance": ", ".join([j.name for j in i.crisis_assistance.all()]),
        } for i in latest_crisis
        ]
    print(payload)
    return payload

class CronEmail(CronJobBase):
    RUN_EVERY_MINS = 1
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronEmail'
    def do(self):
        url = "http://notification:8000/reports/"
        payload = construct_report_data()
        headers = {'Content-Type': "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        # logger.info(response.text)
        logger.info('Sent email to President Office.')

class CronSocialMedia(CronJobBase):
    RUN_EVERY_MINS = 1
    ALLOW_PARALLEL_RUNS = True
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.CronSocialMedia'
    def do(self):
        url = "http://notification:8000/socialmessages/"
        payload = construct_report_data()
        headers = {'Content-Type': "application/json"}
        response = requests.request("POST", url, json=payload, headers=headers)
        # logger.info(response.text)
        logger.info('Sent message to social medias.')
