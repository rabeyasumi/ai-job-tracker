from django.contrib import admin
from .models import JobApplication


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

