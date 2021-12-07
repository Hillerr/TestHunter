from django.urls import path
from . import views

urlpatterns = [
    path('new_client/', views.new_client, name='new_client'),
    path('client_detail/<int:client_id>/', views.client_detail, name='client_detail'),
    path('clients', views.clients, name='clients'),
    path('my_clients', views.my_clients, name='my_clients')
]