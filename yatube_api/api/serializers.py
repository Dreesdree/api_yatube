from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    post = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
