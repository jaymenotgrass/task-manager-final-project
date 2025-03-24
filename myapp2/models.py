from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.
# class Task(models.Model):
#     title = models.CharField(max_length=550)
#     description = models.TextField(max_length=150)
#     due_date = models.DateField(default=timezone.localdate)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    

#     def __str__(self):
#         return self.title
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Optional bio field

    
    preferred_view = models.CharField(
        max_length=10,
        choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('list', 'List')],
        default='daily'
    )
    theme_preference = models.CharField(
        max_length=10,
        choices=[('light', 'Light'), ('dark', 'Dark')],
        default='light'
    )
    receive_notifications = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    


