from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'job_type', 'salary', 'is_active', 'posted_date')
    list_filter = ('job_type', 'is_active')
    search_fields = ('title', 'description', 'location')



