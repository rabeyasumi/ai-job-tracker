from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('applications/', views.application_list, name='application_list'),
    path('applications/add/', views.application_create, name='application_create'),
    path('applications/<int:pk>/', views.application_detail, name='application_detail'),
    path('applications/<int:pk>/edit/', views.application_update, name='application_update'),

    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='jobs/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'applications/<int:pk>/delete/',
        views.application_delete,
        name='application_delete'
    ), 
    path('interviews/', views.interview_list, name='interview_list'),
    path(
        'applications/<int:application_id>/interviews/add/',
        views.interview_create,
        name='interview_create',
    ),
    path('interviews/<int:pk>/edit/', views.interview_update, name='interview_update'),
    path('interviews/<int:pk>/delete/', views.interview_delete, name='interview_delete'), 
    path(
        'applications/<int:pk>/analyze/',
        views.analyze_application,
        name='analyze_application'
    ),
]
