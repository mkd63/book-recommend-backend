from django.db import models
from comments.models import Comments
from users.models import Users

class CommentUpvotes(models.Model):
    comment = models.ForeignKey(Comments, related_name="comment_upvote_post", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Users, related_name="comment_upvote_user", null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["comment", "user"]

    def __str__(self):
        return self.name
