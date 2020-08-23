from django.contrib.auth import get_user_model
from django import forms

from .models import Profile

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'date_of_birth',)
