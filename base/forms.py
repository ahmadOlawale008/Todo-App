from django import forms
from .models import Task, Category
from django.contrib.auth.models import User
# from django.forms import forms
class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control input', 'placeholder': 'Your task...'}))
    time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-group', 'type': 'datetime-local'}))
    completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'checkbox px-5', 'type':'checkbox'}), required=False)
    def clean(self):
        all_cleaned_data = super().clean()
        title = all_cleaned_data['title']
        description = all_cleaned_data['description']
        if len(str(title)) < 1:
            return forms.ValidationError('Please ensure that you have typed a title')
        if len(str(description)) < 1:
            return forms.ValidationError('Please ensure that you have typed a title')
    class Meta:
        model = Task
        fields = ('title', 'description', 'time', 'completed')


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'password')