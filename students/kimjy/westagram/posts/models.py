from django.db import models

from users.models               import User 
from westagram.time_stamp_model import TimeStampModel

class Post(TimeStampModel):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    post_description = models.TextField(null=True)

    class Meta:
        db_table = "posts"


class PostImage(TimeStampModel):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_image = models.CharField(max_length=1000)

    class Meta:
        db_table = "post_images"


class Comment(models.Model):
    post       = models.ForeignKey(Post, on_delete=models.CASCADE)
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    like       = models.BooleanField(default=False)
    comment    = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
