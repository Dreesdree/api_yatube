from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        model = Post


def validate(data):
    if data['text'] == data['']:
        raise serializers.ValidationError(
            'Нельзя сохранять пустой коменнтарий.')
    return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        fields = "__all__"
        model = Comment
        validators = [UniqueTogetherValidator(
            queryset=Comment.objects.all(), fields=['text'])]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
