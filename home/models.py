from django.db import models
from django.utils import timezone


# Create your models here.
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Task(models.Model):
    taskTitle = models.CharField(max_length=300)
    taskDesc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.taskTitle
