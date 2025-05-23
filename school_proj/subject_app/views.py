from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Subject
from .serializers import SubjectSerializer

# Create your views here.
class All_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects, many=True)
        return Response(subjects.data)