from django.urls import path
from . import views

app_name='timecard'
urlpatterns = [
    path('', views.timecard, name='index'),
]