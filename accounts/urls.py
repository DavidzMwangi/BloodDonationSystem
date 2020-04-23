from django.urls import path, include

from accounts.views import register, DashboardView

app_name = 'Accounts'
urlpatterns = [
    path('register', register, name='register'),
    path('dashboard',DashboardView.as_view(), name='dashboard')
]