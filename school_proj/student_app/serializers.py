from rest_framework import serializers
from .models import Student
from subject_app.serializers import SubjectSerializer

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "student_email", "locker_number"]


class StudentAllSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # exclude = ['id']
        fields = ['name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']

    
    def get_subjects(self, instance):
        subjects = instance.subjects.all()
        subjects_ser = SubjectSerializer(subjects, many=True)
        return subjects_ser.data