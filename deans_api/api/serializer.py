from .models import (
	Crisis,
	CrisisAssistance,
	CrisisType
	)
from rest_framework import serializers
from django.utils.timezone import now
from .models.Crisis import STATUS_CHOICES
from django.contrib.auth.models import User


class CrisisAssistanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = CrisisAssistance
		fields = ('id','name',)

class CrisisTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CrisisType
		fields = ('id','name',)

class CrisisSerializer(serializers.ModelSerializer):
	crisis_type = serializers.PrimaryKeyRelatedField(many=True, queryset=CrisisType.objects.all())
	crisis_assistance = serializers.PrimaryKeyRelatedField(many=True, queryset=CrisisAssistance.objects.all())
	class Meta:
		model = Crisis
		fields = (
					'crisis_id',
					'crisis_type',
					'crisis_description',
					'crisis_assistance',
					'crisis_status',
					'crisis_time',
					'crisis_location'
				)

class AdminUserCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username')

class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	
	def create(self, validated_data):
		user = User.objects.create_user(
			username=validated_data['username']
		)
		user.is_staff = validated_data['is_staff']
		user.set_password(validated_data['password'])
		user.save()
		return user

	class Meta:
		model = User