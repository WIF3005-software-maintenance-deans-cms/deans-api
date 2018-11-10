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
    try:
        if sender.dispatch_trigger:
            this_crisis = Crisis.objects.get()
            phone_number_to_notify = json.loads(this_crisis.phone_number_to_notify)

            # TODO: create message

            for phone_number in phone_number_to_notify:
                prefixed_phone_number = "+65" + str(phone_number)
                requests.post("http://notification:8000/dispatchnotices/",
                            json={"number" : prefixed_phone_number, "message" : "go go go, Fire"},
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

