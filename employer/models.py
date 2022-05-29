from django.db import models
class Jobs(models.Model):
    job_title_name=models.CharField(max_length=150)
    company_name=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    salary=models.PositiveIntegerField(null=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title_name

# Create your models here.
# print jobs with exper >1
# exp__lte=1   exp__lt=1
# exp__gte=1   exp__gt=1