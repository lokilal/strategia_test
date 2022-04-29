from rest_framework import serializers
from mptt.templatetags.mptt_tags import cache_tree_children

from .models import Post, Comment

MAX_DEPTH = 5


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField(
        'get_children'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), required=False
    )

    def get_children(self, comment):
        children = comment.get_children()
        if comment.get_level() >= MAX_DEPTH:
            return []
        return CommentSerializer(
            children, many=True
        ).data

    class Meta:
        model = Comment
        exclude = ('lft', 'rght', 'tree_id')
        read_only_fields = ('lft', 'rght', 'tree_id', 'level', 'children')


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(
        'get_comments'
    )

    def get_comments(self, post):
        comments = cache_tree_children(
            Comment.objects.filter(
                post=post, level__lte=MAX_DEPTH
            )
        )
        serializer = CommentSerializer(
            comments, many=True
        )
        return serializer.data

    class Meta:
        model = Post
        fields = '__all__'
