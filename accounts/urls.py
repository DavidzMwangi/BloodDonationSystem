from django.urls import path, include

from accounts.views import register, DashboardView, DonatorReceiverDashboardView, loginRequest

app_name = 'Accounts'
urlpatterns = [
    path('register', register, name='register'),
    path('login', loginRequest, name='login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('user_dashboard', DonatorReceiverDashboardView.as_view(), name='user_dashboard')
]