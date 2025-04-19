# jobs/urls.py

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)  # This makes /jobs/ and /jobs/<id>/ automatically.

urlpatterns = [
    path('', include(router.urls)),
]
