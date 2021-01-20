from django.db import models

# Create your models here.
# entity - models.Model 상속
class Todo(models.Model):
    content = models.CharField(max_length=255) 
    objects = models.Manager()