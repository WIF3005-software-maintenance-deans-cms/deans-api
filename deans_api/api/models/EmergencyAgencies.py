from django.db import models

class EmergencyAgencies(models.Model):
	agency = models.charField(default=None, max_length=255)
	phone_number = models.charField(default=None, max_length=255)
	def __str__(self):
		return self.phone_number

	class Meta:
		pass