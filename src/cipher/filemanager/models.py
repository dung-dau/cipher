from django.db import models

# Create your models here.
class File(models.Model):
	name = models.CharField(max_length=500)
	contents = models.CharField(max_length=1000)