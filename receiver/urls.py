from django.urls import path

from receiver.views import index

urlpatterns = [
    path('test',index)
    
]