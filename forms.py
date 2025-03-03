from django.contrib.auth.forms import UserCreationForm
from django import forms 

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'preferred_view', 'theme_preference', 'receive_notifications']
        
    # Adding widgets for better form presentation
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': 4}), required=False)
    preferred_view = forms.ChoiceField(choices=UserProfile._meta.get_field('preferred_view').choices)
    theme_preference = forms.ChoiceField(choices=UserProfile._meta.get_field('theme_preference').choices)
    receive_notifications = forms.BooleanField(initial=True, required=False)
