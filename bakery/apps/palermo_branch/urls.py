from django.urls import path

from .views import get_patients

app_name = 'palermo_branch'

urlpatterns = [
    path('', get_patients, name='get_patients'),
]


