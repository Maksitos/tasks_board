from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        (1, 'New'),
        (2, 'In progress'),
        (3, 'In QA'),
        (4, 'Ready'),
        (5, 'Done'),
    ]
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='creatorUser')
    performer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='performerUser', blank=True)
    text = models.TextField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.time = timezone.now()
        super().save(*args, **kwargs)


