from django.urls import path

from donator.views import indexView

urlpatterns = [
    path('test',indexView)
]