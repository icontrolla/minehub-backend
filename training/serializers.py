# training/serializers.py

from rest_framework import serializers
from .models import Course

class TrainingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
