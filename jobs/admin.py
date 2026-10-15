from django.contrib import admin
from .models import JobApplication, Interview


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'job_title',
        'company_name',
        'user',
        'status',
        'application_date',
    )

    list_filter = ('status', 'application_date')
    search_fields = ('job_title', 'company_name', 'location')
    ordering = ('-created_at',)
@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'interview_date',
        'interview_type',
    )

    list_filter = ('interview_type', 'interview_date')
    search_fields = (
        'application__job_title',
        'application__company_name',
    )
    ordering = ('interview_date',)

