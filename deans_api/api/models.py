from django.db import models


class Operator(models.Model):
	operator_id = models.IntegerField()
	operator_password = models.CharField(max_length=20)
	operator_name = models.CharField(max_length=30)
	is_admin = models.BooleanField()
	crisis = models.ManyToManyField('Crisis')
	class Meta:
		ordering =['-Operator_Id']
    
class Crisis(models.Model):
	crisis_id = models.AutoField(primary_key=True)
	crisis_type = models.ForeignKey('CrisisType',on_delete=models.CASCADE)
	crisis_cescription = models.TextField()
	crisis_assitance = models.CharField(max_length=30)
	crisis_status = models.ForeignKey('Status',on_delete=models.CASCADE)
	crisis_time = models.DateTimeField(auto_now_add=True)
	crisis_location = models.TextField()
	class Meta:
		ordering =['-Crisis_Id']

class CrisisType (models.Model):
	name=models.CharField(
		choices=('Injury','Hazardous Air Condition','Fire Breakout','Gas Leaks','Crisis Not Listed'),
		default=other)
	class Meta:
		pass
class Status(models.Model):
	name=models.CharField(
		choices=('Pending','Dispatched','Resolved',),
		)
	class Meta:
		pass

