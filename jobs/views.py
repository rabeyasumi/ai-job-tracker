from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import JobApplication, Interview
from .forms import JobApplicationForm, RegistrationForm, InterviewForm
from django.db.models import Count

from .ai_service import analyze_job_description



@login_required
def application_list(request):
    applications = JobApplication.objects.filter(
        user=request.user
    ).order_by('-created_at')

    query = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()
    location = request.GET.get('location', '').strip()

    if query:
        applications = applications.filter(
            models.Q(job_title__icontains=query)
            | models.Q(company_name__icontains=query)
        )

    if status:
        applications = applications.filter(status=status)

    if location:
        applications = applications.filter(
            location__icontains=location
        )

    context = {
        'applications': applications,
        'query': query,
        'selected_status': status,
        'location_query': location,
        'status_choices': JobApplication.STATUS_CHOICES,
    }

    return render(
        request,
        'jobs/application_list.html',
        context
    )



@login_required
def application_detail(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        'jobs/application_detail.html',
        {'application': application}
    )


@login_required
def application_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            return redirect('application_list')
    else:
        form = JobApplicationForm()

    return render(
        request,
        'jobs/application_form.html',
        {'form': form, 'page_title': 'Add Job Application'}
    )


@login_required
def application_update(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        form = JobApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():
            form.save()
            return redirect(
                'application_detail',
                pk=application.pk
            )
    else:
        form = JobApplicationForm(instance=application)

    return render(
        request,
        'jobs/application_form.html',
        {'form': form, 'page_title': 'Edit Job Application'}
    )

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(
        request,
        'jobs/register.html',
        {'form': form}
    )

@login_required
def application_delete(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    if request.method == 'POST':
        application.delete()
        return redirect('application_list')

    return render(
        request,
        'jobs/application_confirm_delete.html',
        {'application': application}
    )
@login_required
def dashboard(request):
    applications = JobApplication.objects.filter(user=request.user)

    total_applications = applications.count()

    status_counts = applications.values('status').annotate(
        total=Count('id')
    )

    status_count_map = {
        item['status']: item['total']
        for item in status_counts
    }

    status_statistics = [
        {
            'value': value,
            'label': label,
            'count': status_count_map.get(value, 0),
        }
        for value, label in JobApplication.STATUS_CHOICES
    ]

    recent_applications = applications.order_by('-created_at')[:5]
    upcoming_interviews = Interview.objects.filter(
        application__user=request.user,
        interview_date__gte=timezone.now()
    ).select_related('application').order_by('interview_date')[:5]

    context = {
        'total_applications': total_applications,
        'status_statistics': status_statistics,
        'recent_applications': recent_applications,
        'upcoming_interviews': upcoming_interviews,
    }

    return render(request, 'jobs/dashboard.html', context)

@login_required
def interview_list(request):
    interviews = Interview.objects.filter(
        application__user=request.user
    ).select_related('application').order_by('interview_date')

    return render(
        request,
        'jobs/interview_list.html',
        {'interviews': interviews}
    )


@login_required
def interview_create(request, application_id):
    application = get_object_or_404(
        JobApplication,
        pk=application_id,
        user=request.user
    )

    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.application = application
            interview.save()
            return redirect('interview_list')
    else:
        form = InterviewForm()

    return render(request, 'jobs/interview_form.html', {
        'form': form,
        'application': application,
        'page_title': 'Add Interview',
    })


@login_required
def interview_update(request, pk):
    interview = get_object_or_404(
        Interview,
        pk=pk,
        application__user=request.user
    )

    if request.method == 'POST':
        form = InterviewForm(request.POST, instance=interview)
        if form.is_valid():
            form.save()
            return redirect('interview_list')
    else:
        form = InterviewForm(instance=interview)

    return render(request, 'jobs/interview_form.html', {
        'form': form,
        'application': interview.application,
        'page_title': 'Edit Interview',
    })


@login_required
def interview_delete(request, pk):
    interview = get_object_or_404(
        Interview,
        pk=pk,
        application__user=request.user
    )

    if request.method == 'POST':
        interview.delete()
        return redirect('interview_list')

    return render(request, 'jobs/interview_confirm_delete.html', {
        'interview': interview,
    })

@login_required
def analyze_application(request, pk):
    application = get_object_or_404(
        JobApplication,
        pk=pk,
        user=request.user
    )

    analysis = None
    error = None

    if request.method == 'POST':
        if not application.job_description.strip():
            error = "This application has no job description to analyze."
        else:
            try:
                analysis = analyze_job_description(
                    application.job_description
                )
            except Exception as e:
                print("AI ANALYSIS ERROR:", repr(e))
                error = (
                    "AI analysis failed. Check the VS Code terminal "
                    "for the actual error."
                )

    return render(
        request,
        'jobs/ai_analysis.html',
        {
            'application': application,
            'analysis': analysis,
            'error': error,
        }
    )