from django.db import models

class EmergencyAgencies(models.Model):
	agency = models.CharField(default=None, max_length=255)
	phone_number = models.CharField(default=None, max_length=255)
	def __str__(self):
		return self.agency

	class Meta:
		pass