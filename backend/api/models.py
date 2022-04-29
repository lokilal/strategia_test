import mptt.fields
from django.db import models
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )


class Comment(MPTTModel):
    text = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    parent = mptt.fields.TreeForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )

