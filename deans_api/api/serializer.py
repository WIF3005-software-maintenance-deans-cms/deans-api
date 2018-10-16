from api.models import Crisis
from rest_framework import serializers

class CrisisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crisis
        fields = ('Crisis_Id,Crisis_Category,Crisis_Description,Crisis_Assitance,Crisis_Status,Crisis_Time,Crisis_Location')

# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('url', 'id', 'name', 'posts')
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'posts')