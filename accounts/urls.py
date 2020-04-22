from django.urls import path, include

from accounts.views import register
app_name = 'Accounts'
urlpatterns = [
    path('register', register, name='register')
]