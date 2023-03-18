from Mobile.views import *
from django.urls import path
app_name='Mobile'

urlpatterns=[
    path('Fourth/',Fourth,name='Fourth'),
    path('Fifth/',Fifth,name='Fifth'),
    path('Six/',Six,name='Six'),
]