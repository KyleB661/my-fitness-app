from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Workout, Exercise

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a username'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create a password'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Choose a username (150 characters or fewer)'
        self.fields['password1'].help_text = 'Your password must be at least 8 characters long'
        self.fields['password2'].help_text = 'Enter the same password as before'

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'date', 'duration', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.01'}),
        }