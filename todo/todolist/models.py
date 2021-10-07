from django.db import models
from django.utils import timezone
from django.conf import settings
class Profile(models.Model):
    CHOICES = (
        ('Edit', 'Edit'),
        ('Delete', 'Delete'),
        ('Add', 'Add'),
    )
    username = models.CharField(max_length=300)
    options = models.CharField(max_length=300, choices = CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.username 
