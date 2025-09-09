from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='show_main'),
]
