from django.db import models
from django.utils import timezone
from django.conf import settings
# class Profile(models.Model):
#     CHOICES = (
#         ('Edit', 'Edit'),
#         ('Delete', 'Delete'),
#         ('Add', 'Add'),
#     )
#     username = models.CharField(max_length=300)
#     options = models.CharField(max_length=300, choices = CHOICES)
#     created_date = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.username 
from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title