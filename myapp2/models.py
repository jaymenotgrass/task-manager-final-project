from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    #status = models.

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)  # Optional bio field

    #Task Manager specific fields
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
    


