from django.db import models

# Create your models here.


# Feedback Form Models
class Feedback(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(default='', max_length=120)
    subject = models.CharField(default='', max_length=120)
    message = models.TextField(default='')

    def __str__(self):
        return self.username

