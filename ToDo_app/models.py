import uuid
from django.db import models

# Create your models here.



class Task(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('incomplete', 'Incomplete'),
        ('onprogress', 'On Progress'),
    ]
    task_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    priority=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='incomplete',
    )
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    