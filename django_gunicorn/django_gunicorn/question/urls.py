from django.urls import path
from .views import *

urlpatterns = [
    path('', question, name='questions'),
]