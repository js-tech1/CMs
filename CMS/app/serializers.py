from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    # def create(self, validated_data):
    #     validated_data['owner'] = self.context['request'].user
    #     return super().create(validated_data)   

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

    