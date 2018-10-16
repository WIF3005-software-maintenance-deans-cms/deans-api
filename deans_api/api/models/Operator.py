from django.contrib.auth.models import User 
from django.db import models

class Operator(models.Model):
	operator_id = models.IntegerField()
	operator_password = models.CharField(max_length=20)
	operator_name = models.CharField(max_length=30)
	is_admin = models.BooleanField()
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	crisis = models.ManyToManyField('Crisis')
	
	def __utf8__(self):
		return self.operator_id
		
	class Meta:
		ordering =['-operator_id']