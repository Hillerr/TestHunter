from django.urls import path
from . import views

urlpatterns = [
    path('new_test/', views.new_test, name='new_test'),
    path('tests/', views.tests, name='tests'),
]