from django.db import models
from posts.models import Posts
from users.models import Users

class Comments(models.Model):
    content = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Posts, related_name="comment_post", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Users, related_name="comment_user", null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
