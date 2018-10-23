from django.db import models
    
    
class CrisisType (models.Model):
	name=models.ListCharField(base_field=CharField(max_length=20),
			size=20,
			default=None,
			max_length=(20*20))
	
	def __str__(self):
		return self.name

	class Meta:
		pass