from .models import (
	Crisis,
	CrisisAssistance,
	CrisisType
	)
from rest_framework import serializers
from django.utils.timezone import now
from .models.Crisis import STATUS_CHOICES
from django.contrib.auth.models import User

# class CrisisUpdateSerializer(serializers.ModelSerializer):
# 	crisis_id = serializers.IntegerField(read_only=True)
# 	crisis_type = serializers.HyperlinkedRelatedField(
# 		view_name='CrisisType-detail',
# 		lookup_field='name')
# 	crisis_description = serializers.CharField(required=False, allow_blank=True, max_length=255)
# 	crisis_assistance = serializers.CharField(max_length=30)
# 	crisis_time = serializers.DateTimeField(auto_now_add=True)
# 	crisis_location = serializers.CharField(required=False, allow_blank=False, max_length=100)
# 	updated_at = serializers.DateTimeField(auto_now_add=True)
# 	crisis_status = serializers.ChoiceField(choices=STATUS_CHOICES, default='Pending')

# 	class Meta:
# 		model = Crisis
# 		fields = (
# 			'crisis_id',
# 			'crisis_type',
# 			'crisis_description',
# 			'crisis_assistance',
# 			'crisis_time',
# 			'crisis_location',
# 			'updated_at'
# 		)
# 		read_only_fields=('id', 'updated_at',)

# 	def update(self, instance, validated_data):
# 		# Update fields if there is any change
# 		for field, value in validated_data.items():
# 			setattr(instance, field, value)
# 		# Update 'updated_at' field to now
# 		setattr(instance, 'updated_at', now())

# 		# Note: If user update post, it won't change the last_activity
# 		instance.save()
# 		return instance

class CrisisAssistanceSerializer(serializers.ModelSerializer):
	class Meta:
		model = CrisisAssistance
		fields = ('name',)

class CrisisTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CrisisType
		fields = ('name',)



# class CrisisDeleteSerializer(serializers.ModelSerializer):
# 	# TODO: code this
# 	class Meta:
# 		model = Crisis
# 		fields = '__all__'

class CrisisSerializer(serializers.ModelSerializer):
	# crisis_type = CrisisTypeSerializer(read_only=True, many=True)
	crisis_type = serializers.PrimaryKeyRelatedField(many=True, queryset=CrisisType.objects.all())
	crisis_assistance = serializers.PrimaryKeyRelatedField(many=True, queryset=CrisisAssistance.objects.all())
	# persons = serializers.PrimaryKeyRelatedField(
	#        many=True, queryset=Person.objects.all())
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