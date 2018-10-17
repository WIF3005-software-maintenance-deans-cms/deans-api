from django.contrib.auth.models import User 
from django.db import models
from .CrisisType import CrisisType
STATUS_CHOICES = (
	('PD', 'Pending'),
	('DP', 'Dispached'),
	('RS', 'Resolved'),
)

class Crisis(models.Model):
	crisis_id = models.AutoField(primary_key=True)
	crisis_type = models.ForeignKey('CrisisType',on_delete=models.CASCADE)
	crisis_description = models.TextField()
	crisis_assistance = models.CharField(max_length=30)
	crisis_time = models.DateTimeField(auto_now_add=True)
	crisis_location = models.TextField()
	updated_at = models.DateTimeField(auto_now_add=True)


	crisis_status = models.CharField(choices=STATUS_CHOICES, default='PD',  max_length=254)

	def __utf8__(self):
		return self.crisis_id

	class Meta:
		ordering =['-crisis_id']

