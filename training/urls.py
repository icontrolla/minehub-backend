from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TrainingCourseViewSet, create_checkout_session

router = DefaultRouter()
router.register(r'training-courses', TrainingCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
]
