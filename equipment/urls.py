from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    DrillingMachineViewSet,
    ExcavatorViewSet,
    LoaderViewSet,
    TransportTruckViewSet,
    CartView,
    AddToCartView,
    RemoveFromCartView,
    UpdateCartItemView,
)

router = DefaultRouter()
router.register(r'drilling-machines', DrillingMachineViewSet)
router.register(r'excavators', ExcavatorViewSet)
router.register(r'loaders', LoaderViewSet)
router.register(r'transport-trucks', TransportTruckViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Cart API endpoints
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/update/', UpdateCartItemView.as_view(), name='update-cart-item'),
]
