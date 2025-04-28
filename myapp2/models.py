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
    # Choices for preferred view and theme
    PREFERRED_VIEW_CHOICES = [
        ('list', 'List View'),
        ('grid', 'Grid View'),
    ]
    THEME_CHOICES = [
        ('light', 'Light Theme'),
        ('dark', 'Dark Theme'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    preferred_view = models.CharField(max_length=10, choices=PREFERRED_VIEW_CHOICES, default='list')
    theme_preference = models.CharField(max_length=5, choices=THEME_CHOICES, default='light')
    receive_notifications = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    


