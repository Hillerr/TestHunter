from django.urls import path
from . import views

urlpatterns = [
    path('new_test/', views.new_test, name='new_test'),
    path('', views.tests, name='tests'),
    path('test_detail/<int:test_id>', views.test_detail, name='test_detail'),
    path('my_tests/', views.my_tests, name='my_tests')
]