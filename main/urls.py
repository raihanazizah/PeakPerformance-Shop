from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
