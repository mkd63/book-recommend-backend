from django.db import models
from posts.models import Posts
from users.models import Users

class Upvotes(models.Model):
    post = models.ForeignKey(Posts, related_name="upvote_post", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Users, related_name="upvote_user", null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["post", "user"]

    def __str__(self):
        return self.name
