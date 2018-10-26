from django.db.models import Model, CharField
class CrisisAssistance (Model):
	name=CharField(
			default=None,
			max_length=(255))

	def __str__(self):
		return str(self.name)

	class Meta:
		pass