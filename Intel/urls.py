from Intel.views import *
from django.urls import path
app_name='Intel'

urlpatterns=[
    path('Keypad/',Keypad,name='Keypad'),
    path('Computer/',Computer,name='Computer'),
]