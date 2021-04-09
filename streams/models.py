from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Stream(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.CharField('Description', max_length=200)
    link = models.URLField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
