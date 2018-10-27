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
                    'your_name',
                    'mobile_number',
                    'crisis_type',
                    'crisis_description',
                    'crisis_assistance',
                    'crisis_status',
                    'crisis_time',
                    'crisis_location1',
                    'crisis_location2'
                )
                
class CrisisBasicSerializer(serializers.ModelSerializer):
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
                    'crisis_location1',
                    'crisis_location2'
                )

class CrisisUpdateSerializer(serializers.ModelSerializer):
    # content = serializers.CharField(required=True)
    # thread = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='thread-detail'
    # )
    # creator = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='user-detail',
    #     lookup_field='username'
    # )
    class Meta:
        model = Crisis
        fields = (
            'crisis_type',
            'your_name',
            'mobile_number',
            'crisis_description',
            'crisis_assistance',
            'crisis_status',
            'crisis_location1',
            'crisis_location2'
        )

    def update(self, instance, validated_data):
        # Update fields if there is any change
        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Update 'updated_at' field to now
        setattr(instance, 'updated_at', now())

        # Note: If user update post, it won't change the last_activity
        instance.save()
        return instance

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
        fields = ('id', 'username', 'password', 'is_staff')