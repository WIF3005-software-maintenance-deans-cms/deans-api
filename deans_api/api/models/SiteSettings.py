from django.db import models

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
    support = models.EmailField(default='support@example.com')
    sales_department = models.EmailField(blank=True)
    twilio_account_sid = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')
    twilio_auth_token = models.CharField(max_length=255, default='abd4d45dd57dd79b86dd51df2e2a6cd5')
    twilio_phone_number = models.CharField(max_length=255, default='+15006660005')

