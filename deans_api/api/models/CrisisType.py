from django.db import models
    
    
class CrisisType (models.Model):
	name=models.CharField(
			default=None,
			max_length=255)
	
	def __str__(self):
		return self.name

	class Meta:
		pass