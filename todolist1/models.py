from django.db import models

# Create your models here.
class Todolist(models.Model):
    task = models.CharField(max_length=20)