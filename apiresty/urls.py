# urls.py

from django.urls import path
from .views import index, StudentView, Student_detail,create_grade
urlpatterns = [
    path('api/students/', StudentView.as_view(), name='grade-list-create'),
    path('api/student/<int:pk>/', Student_detail, name='grade-retrieve-update-destroy'),
    # Add other URLs as needed
    path('', index),
    path('grade/', create_grade, name='create_grade')
]