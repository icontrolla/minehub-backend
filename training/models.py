from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    duration_days = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    instructor_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title
