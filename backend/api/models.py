import mptt.fields
from django.db import models
from mptt.models import MPTTModel


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        auto_now_add=True
    )
    author = models.CharField(
        max_length=256
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
    author = models.CharField(
        max_length=256
    )

