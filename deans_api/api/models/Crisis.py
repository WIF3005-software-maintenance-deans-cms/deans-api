from django.contrib.auth.models import User 
from django.db import models
from .CrisisType import CrisisType
from .Operator import Operator
from .CrisisAssistance import CrisisAssistance
from django.db.models import signals
import requests

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
    crisis_description = models.TextField()
    crisis_assistance = models.ManyToManyField(CrisisAssistance)
    crisis_assistance_description = models.TextField()
    crisis_time = models.DateTimeField(auto_now_add=True)
    crisis_location1 = models.TextField()
    crisis_location2 = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ManyToManyField(User)
    visible = models.BooleanField(default=True)

    dispatch_trigger = models.BooleanField(default=False)
    # TODO: support visible in backend

    crisis_status = models.CharField(choices=STATUS_CHOICES, default='PD',  max_length=254)

    def __str__(self):
        return str(self.crisis_id)

    class Meta:
        ordering = ['-crisis_id']

def dispatch_trigger(sender, instance, created, **kwargs):

    if sender.dispatch_trigger:
        requests.post("http://notification:8000/dispatchnotices/",
                      json={"number" : "+6586963013", "message" : "go go go, Fire"},
                      headers={
                        'content-type': "application/json",
                        'cache-control': "no-cache"
                      }
                      )

signals.post_save.connect(receiver=dispatch_trigger, sender=Crisis)

