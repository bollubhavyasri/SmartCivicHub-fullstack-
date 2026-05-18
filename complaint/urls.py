from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),

    path('main/', views.mainpage, name='mainpage'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('submit/', views.submit_complaint, name='submit'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('update-status/<int:id>/', views.update_status, name='update_status'),
    
]