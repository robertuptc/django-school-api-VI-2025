from django.urls import path
from .views import All_student

urlpatterns = [
    path('', All_student.as_view(), name="all_students")
]