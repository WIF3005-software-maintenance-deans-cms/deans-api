from django.contrib.auth.models import User 
from django.db import models
from .CrisisType import CrisisType
from .Operator import Operator
from .CrisisAssistance import CrisisAssistance
from django.db.models import signals
import requests
import channels.layers
from asgiref.sync import async_to_sync
from rest_framework.response import Response # this is bad!
import json

STATUS_CHOICES = (
    ('PD', 'Pending'),
    ('DP', 'Dispatched'),
    ('RS', 'Resolved'),
)

class Crisis(models.Model):
    your_name = models.CharField(default=None,max_length=255)
    mobile_number = models.CharField(default=None,max_length=255)
    crisis_id = models.AutoField(primary_key=True)
    crisis_type = models.ManyToManyField(CrisisType)
    crisis_description = models.TextField(default="")
    crisis_assistance = models.ManyToManyField(CrisisAssistance)
    crisis_assistance_description = models.TextField(default="")
    crisis_time = models.DateTimeField(auto_now_add=True)
    crisis_location1 = models.TextField()
    crisis_location2 = models.TextField(default="")
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ManyToManyField(User)
    visible = models.BooleanField(default=True)
    phone_number_to_notify = models.CharField(default="",max_length=255)
    dispatch_trigger = models.BooleanField(default=False)
    # TODO: support visible in backend

    crisis_status = models.CharField(choices=STATUS_CHOICES, default='PD',  max_length=254)

    def __str__(self):
        return str(self.crisis_id)

    class Meta:
        ordering = ['-crisis_id']

def trigger(sender, instance, created, **kwargs):
    this_crisis = Crisis.objects.get()
    crisis_status = this_crisis.crisis_status;
    if crisis_status == "DP":
        try:
            if sender.dispatch_trigger:
                this_crisis = Crisis.objects.get()
                phone_number_to_notify = json.loads(this_crisis.phone_number_to_notify)
                # start creating message
                reported_time = str(this_crisis.crisis_time)
                name = this_crisis.your_name
                mobile_number = this_crisis.mobile_number
                location1 = this_crisis.crisis_location1
                location2 = this_crisis.crisis_location2
                # create crisis type
                crisis_type_queryset = this_crisis.crisis_type.all()
                crisis_type = []
                for _ in crisis_type_queryset:
                    crisis_type.append(str(_))
                crisis_type = ", ".join(crisis_type)
                # create assistance type
                assistance_type_queryset = this_crisis.crisis_assistance.all()
                assistance_type = []
                for _ in assistance_type_queryset:
                    assistance_type.append(str(_))
                assistance_type = ", ".join(assistance_type)
                # handle the rest
                crisis_description = this_crisis.crisis_description
                assistance_description = this_crisis.crisis_assistance_description
                # construct message content
                message = "We have received the following crisis report, need your immediate action:\n\n"
                message += "Reported Time: " + reported_time + "\n"
                message += "Reporter Name: " + name + "\n"
                message += "Mobile Number: " + mobile_number + "\n"
                message += "Location: " + location1 + "\n"
                message += "Location2: " + location2 + "\n"
                message += "Crisis Type: " + crisis_type + "\n"
                message += "Crisis Description: " + crisis_description + "\n"
                message += "Requested Assistance: " + assistance_type + "\n"
                message += "Assistance Description: " + assistance_description + "\n"
                message += "\nThank you for keeping our people safe!"

                print(message)

                for phone_number in phone_number_to_notify:
                    prefixed_phone_number = "+65" + str(phone_number)
                    requests.post("http://notification:8000/dispatchnotices/",
                                json={"number" : prefixed_phone_number, "message" : message},
                                headers={
                                    'content-type': "application/json",
                                    'cache-control': "no-cache"
                                }
                                )
        except Exception as e:
            print("It is ok.", e)

        try:
            # send to redis
            queryset = Crisis.objects.all()
            from ..serializer import CrisisSerializer # this is bad !
            serializer = CrisisSerializer(queryset, many=True)
            response = Response(serializer.data) # response is an array of crises
            channel_layer = channels.layers.get_channel_layer()
            async_to_sync(channel_layer.group_send)("crises", {
                "type": "crises_update",
                "payload": json.dumps(list(response.data))
            })
        except Exception as e:
            print("It is not ok. Human lives at risk!", e)

signals.post_save.connect(receiver=trigger, sender=Crisis)

