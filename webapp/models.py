from django.db import models
from django.utils import timezone

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateField(default=timezone.now)
    modified_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Item(models.Model):
    task = models.TextField()
    type = models.ForeignKey(List, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task