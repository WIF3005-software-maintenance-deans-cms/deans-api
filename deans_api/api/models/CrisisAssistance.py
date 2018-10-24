from django.db import models
from .EmergencyAgencies import EmergencyAgencies
class CrisisAssistance (models.Model):
	name=models.CharField(
			default=None,
			max_length=255)
	contact_number=models.CharField(default=None,max_length=255)
	agencies=models.ManyToManyField(EmergencyAgencies)
	def __str__(self):
		return self.name

	class Meta:
		pass