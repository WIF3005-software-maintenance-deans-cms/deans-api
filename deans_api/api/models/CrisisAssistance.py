from django.db.models import Model, CharField, ManyToManyField
from django_mysql.models import ListCharField
from .EmergencyAgencies import EmergencyAgencies
class CrisisAssistance (Model):
	name=ListCharField(
			base_field=CharField(max_length=20),
			default=None,
			size=10,
			max_length=(255))
	contact_number=CharField(default=None,max_length=255)
	agencies=ManyToManyField(EmergencyAgencies)
	def __str__(self):
		return self.name

	class Meta:
		pass