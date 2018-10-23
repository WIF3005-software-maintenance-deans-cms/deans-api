from django.db import models
from .CrisisType import CrisisType
from .CrisisAssistance import CrisisAssistance
from .EmergencyAgencies import EmergencyAgencies
from .SocialMediaAccount import SocialMediaAccount
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSettings(SingletonModel):
    setting_type = models.ForeignKey('CrisisType',default = None)
    setting_assistance = models.ForeignKey('CrisisAssistance',default = None)
    social_media_account = models.ForeignKey('SocialMediaAccount', default = None)
    emergency_agencies = models.ForeignKey('EmergencyAgencies', default = None)
    summary_reporting_email = models.EmailField(default='prime-minister@gmail.com')
    
