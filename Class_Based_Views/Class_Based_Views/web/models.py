from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(
        max_length=30
    )
    last_name = models.CharField(
        max_length=30
    )
    seniority_level = models.CharField(
        max_length=30,
        choices=(
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
            ('Senior', 'Senior')
        )
    )