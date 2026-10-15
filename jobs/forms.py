
from django import forms
from .models import JobApplication, Interview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'job_title',
            'company_name',
            'job_description',
            'location',
            'salary',
            'job_url',
            'application_date',
            'status',
            'notes',
        ]

        widgets = {
            'job_description': forms.Textarea(attrs={'rows': 4}),
            'notes': forms.Textarea(attrs={'rows': 3}),
            'application_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email', '')

        if commit:
            user.save()

        return user
    
class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [
            'interview_date',
            'interview_type',
            'location',
            'meeting_link',
            'notes',
        ]

        widgets = {
            'interview_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interview_date'].input_formats = [
            '%Y-%m-%dT%H:%M'
        ]
