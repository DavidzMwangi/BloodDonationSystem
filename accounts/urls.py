from django.urls import path, include

from accounts.views import register, login,DashboardView

app_name = 'Accounts'
urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard',DashboardView.as_view(), name='dashboard')
]