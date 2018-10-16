from .models import Crisis
from rest_framework import serializers

class CrisisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crisis
        fields = (
        			'crisis_id',
        			'crisis_type',
        			'crisis_description',
        			'crisis_assitance',
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