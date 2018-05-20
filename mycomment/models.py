from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class head_comment(models.Model):
    
    title = models.CharField(max_length = 100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    tags = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
    thumb_up = models.ManyToManyField(User, related_name="head_comment_thumb_up")
    thumb_down = models.ManyToManyField(User, related_name="head_comment_thumb_down")
    attention = models.ManyToManyField(User, related_name="head_comment_attention")

    def __str__(self):
        return self.title

class comment(models.Model):
    father = models.ForeignKey(head_comment, on_delete=models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thumb_up = models.ManyToManyField(User, related_name="comment_thumb_up")
    thumb_down = models.ManyToManyField(User, related_name="comment_thumb_down")
    
    def __str__(self):
        return self.content