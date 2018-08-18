from django.db import models


# Create your models here.
class Enterprise(models.Model):
    enterprise_name = models.CharField(
        max_length=100,
        default=''
    )
