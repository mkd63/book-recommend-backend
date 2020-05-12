from django.db import models
# Create your models here.
class Job(models.Model):

    company_name = models.CharField(max_length=100, blank=False, default='')
    role = models.EmailField(max_length = 100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    currently_working = models.BooleanField()
    user = models.ForeignKey('users.Users', on_delete = models.CASCADE)

    def __str__(self):
        return self.name
