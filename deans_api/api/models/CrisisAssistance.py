from django.db import models
    
class CrisisAssistance (models.Model):
	name=models.CharField(
			default=None,
			max_length=255)
	
	def __str__(self):
		return self.name

	class Meta:
		pass