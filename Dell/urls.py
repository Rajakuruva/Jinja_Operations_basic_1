from Dell.views import *
from django.urls import path
app_name='Dell'

urlpatterns=[
    path('Laptop/',Laptop,name='Laptop'),
    path('Phone/',Phone,name='Phone'),
]