from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor_name', 'duration_days', 'price', 'created_at')
    search_fields = ('title', 'instructor_name')

