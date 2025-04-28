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
        fields = 'profile_picture','bio', 'preferred_view', 'theme_preference', 'receive_notifications'
        
   # Adding widgets for better form presentation
    
    # Profile Picture
    profile_picture = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        label='Profile Picture (Optional)'
    )
    
    # Bio field with Textarea
    bio = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': 4, 'class': 'form-control'}),
        required=False,
        label='Your Bio'
    )
    
    # Preferred View as a choice field (with Select widget)
    preferred_view = forms.ChoiceField(
        choices=UserProfile.PREFERRED_VIEW_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Preferred View'
    )
    
    # Theme Preference (Light/Dark)
    theme_preference = forms.ChoiceField(
        choices=UserProfile.THEME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Theme Preference'
    )
    
    # Receive Notifications field (Checkbox)
    receive_notifications = forms.BooleanField(
        initial=True,
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Receive Notifications'
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        
        fields = ['title', 'description', 'due_date', 'completed']

    due_date = forms.DateTimeField(
        widget=DateTimeInput(attrs={'type': 'datetime-local'})
    )