from django.shortcuts import render
from .models import Student
from .serializers import StudentAllSerializer
from rest_framework.views import APIView, Response

# Create your views here.
class All_student(APIView):
    def get(self, request):
        students = StudentAllSerializer(Student.objects, many=True)
        return Response(students.data)