from django.db import models


class Operator(models.Model):
	Operator_Id = models.IntegerField()
	Operator_Password = models.CharField(max_length=20)
	Operator_Name = models.CharField(max_length=30)
	Is_Admin = models.BooleanField()
	crisis = models.ManyToManyField('Crisis')
	class Meta:
		ordering =['-Operator_Id']
    
class Crisis(models.Model):
	Crisis_Id = models.AutoField(primary_key=True)
	Crisis_Category = models.CharField(max_length=30)
	Crisis_Description = models.TextField()
	Crisis_Assitance = models.CharField(max_length=30)
	Crisis_Status = models.CharField(max_length=30)
	Crisis_Time = models.DateTimeField(auto_now_add=True)
	Crisis_Location = models.TextField()
	class Meta:
		ordering =['-Crisis_Id']
