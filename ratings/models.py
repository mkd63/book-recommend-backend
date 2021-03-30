from django.db import models
from users.models import Users
from books.models import Books

class Ratings(models.Model):
    user = models.ForeignKey(Users, related_name="user", null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, related_name="book", null=True, on_delete=models.CASCADE)
    rating = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "book"]
