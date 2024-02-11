# urls.py

from django.urls import path
from .views import index, StudentView, Student_detail

urlpatterns = [
    path('api/grades/', StudentView.as_view(), name='grade-list-create'),
    path('api/grades/<int:pk>/', Student_detail, name='grade-retrieve-update-destroy'),
    # Add other URLs as needed
    path('', index)
]