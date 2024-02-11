from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
   

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
  
    def __str__(self):
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,default=0)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.marks)
