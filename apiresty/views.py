from django.http import HttpResponse
from .models import Student, Grade,Subject
from .serializers import StudentSerializer,GradeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from .forms import GradeForm

class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view

@api_view(['GET'])
def Student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)
    

def index(request):
    return HttpResponse('Hello!!')




def create_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or perform other actions
    else:
        form = GradeForm()
    
    return render(request, 'create_grade.html', {'form': form})