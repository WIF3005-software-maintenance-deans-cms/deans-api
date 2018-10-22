from django.contrib.auth.models import User 
from django.db import models
from .CrisisType import CrisisType
from .Operator import Operator
from .CrisisAssistance import CrisisAssistance

STATUS_CHOICES = (
	('PD', 'Pending'),
	('DP', 'Dispached'),
	('RS', 'Resolved'),
)

class Crisis(models.Model):
	crisis_id = models.AutoField(primary_key=True)
	crisis_type = models.ManyToManyField(CrisisType)
	crisis_description = models.TextField()
	crisis_assistance = models.ManyToManyField(CrisisAssistance)
	crisis_time = models.DateTimeField(auto_now_add=True)
	crisis_location = models.TextField()
	updated_at = models.DateTimeField(auto_now_add=True)
	owner = models.ManyToManyField(User)
	visible = models.BooleanField(default=True) 
	# TODO: support visible in backend

	cripsis_status = models.CharField(choices=STATUS_CHOICES, default='PD',  max_length=254)

	def __str__(self):
		return str(self.crisis_id)

	class Meta:
		ordering =['-crisis_id']

