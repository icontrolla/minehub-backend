# training/views.py
import stripe
from rest_framework import viewsets
from .models import Course
from .serializers import TrainingCourseSerializer
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        data = json.loads(request.body)
        course_id = data.get('course_id')

        from .models import Course
        try:
            course = Course.objects.get(id=course_id)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': course.title,
                        },
                        'unit_amount': int(course.price * 100),
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://localhost:3000/success/',
                cancel_url='http://localhost:3000/cancel/',
            )
            return JsonResponse({'id': session.id})
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found.'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)

class TrainingCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = TrainingCourseSerializer
