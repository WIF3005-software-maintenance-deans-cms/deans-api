from deans_api.api.models import Crisis
from rest_framework import serializers

class CrisisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crisis
        fields = ('url', 'id', 'title', 'pub_time', 'author', 'body', 'tags')

# class TagSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('url', 'id', 'name', 'posts')
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'id', 'username', 'posts')