from .models import Crisis
from rest_framework import serializers
from django.utils.timezone import now
from .models.Crisis import STATUS_CHOICES

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

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    crisis_id = serializers.IntegerField(read_only=True)
    crisis_type = serializers.HyperlinkedRelatedField(
        view_name='CrisisType-detail',
        lookup_field='name')
    crisis_description = serializers.CharField(required=False, allow_blank=True, max_length=255)
    crisis_assistance = serializers.CharField(max_length=30)
    crisis_time = serializers.DateTimeField(auto_now_add=True)
    crisis_location = serializers.CharField(required=False, allow_blank=False, max_length=100)
    updated_at = serializers.DateTimeField(auto_now_add=True)
    crisis_status = serializers.ChoiceField(choices=STATUS_CHOICES, default='Pending')

    class Meta:
        model = Crisis
        fields = (
            'crisis_id',
            'crisis_type',
            'crisis_description',
            'crisis_assistance',
            'crisis_time',
            'crisis_location',
            'updated_at'
        )
        read_only_fields=('id', 'updated_at',)

    def update(self, instance, validated_data):
        # Update fields if there is any change
        for field, value in validated_data.items():
            setattr(instance, field, value)
        # Update 'updated_at' field to now
        setattr(instance, 'updated_at', now())

        # Note: If user update post, it won't change the last_activity
        instance.save()
        return instance


class CrisisDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crisis
        fields = '__all__'


class CrisisListSerializer(serializers.HyperlinkedModelSerializer):
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



# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('url', 'id', 'name', 'posts')
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'posts')