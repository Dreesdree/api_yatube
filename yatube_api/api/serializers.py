from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    post = serializers.ReadOnlyField(source='post.id')
    text = serializers.CharField()

    class Meta:
        fields = '__all__'
        model = Comment

        def validate_text(self, data):
            if not data:
                raise serializers.ValidationError(
                    'Коментарий не должен быть пустым'
                )
            return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
