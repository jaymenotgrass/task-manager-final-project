from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms import DateTimeInput

from .models import UserProfile, Task

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'preferred_view', 'theme_preference', 'receive_notifications']
        
    # Adding widgets for better form presentation
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': 4}), required=False)
    preferred_view = forms.ChoiceField(choices=UserProfile._meta.get_field('preferred_view').choices)
    theme_preference = forms.ChoiceField(choices=UserProfile._meta.get_field('theme_preference').choices)
    receive_notifications = forms.BooleanField(initial=True, required=False)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        
        fields = ['title', 'description', 'due_date', 'completed']

    due_date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'})
    )