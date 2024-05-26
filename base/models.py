from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):    
    id = models.AutoField(primary_key=True)
    user_choices  = [('important', 'Important')]
    user_choice = models.CharField(max_length=15, default=user_choices[0], choices=user_choices)
    def __str__(self):
        return self.user_choices[0][0]
    
class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='task_categorized')
    
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1200)
    time = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at',]
        
    def __str__(self):
        return self.title

    
