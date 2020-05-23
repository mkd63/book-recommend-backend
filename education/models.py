from django.db import models
from users.models import Users

class Education(models.Model):
    institution_name = models.CharField(max_length=100, blank=False, default='')
    qualification_name = models.CharField(max_length = 100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    currently_studying = models.BooleanField()
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
