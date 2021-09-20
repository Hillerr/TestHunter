from django.urls import path
from . import views

urlpatterns = [
    path('new_test/', views.new_test, name='new_test'),
    path('', views.tests, name='tests'),
    path('test_detail/<int:test_id>', views.test_detail, name='test_detail'),
    path('my_tests/', views.my_tests, name='my_tests'),
    path('my_unfinished_tests/', views.my_unfinished_tests, name='my_unfinished_tests'),
    path('edit_test/<int:test_id>', views.edit_test, name='edit_test'),
    path('finish_test/', views.finish_test, name='finish_test'),
    path('remove_test/', views.remove_test, name='remove_test'),

    path('add_test_image/<int:test_id>', views.add_test_image, name='add_test_image'),
    path('remove_test_image/<int:test_id>/<int:image_id>', views.remove_test_image, name='remove_test_image'),
]