from rest_framework import viewsets
from rest_framework import generics
from .models import Equipment, DrillingMachine, Excavator, Loader, TransportTruck
from .serializers import (
    EquipmentSerializer,
    DrillingMachineSerializer,
    ExcavatorSerializer,
    LoaderSerializer,
    TransportTruckSerializer,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.views import APIView

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)

        content_type_id = request.data.get('content_type_id')
        object_id = request.data.get('object_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            content_type = ContentType.objects.get(id=content_type_id)
            machine = content_type.get_object_for_this_type(id=object_id)
        except ContentType.DoesNotExist:
            return Response({'error': 'Invalid machine type.'}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            content_type=content_type,
            object_id=object_id,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return Response({'message': 'Item added to cart.'}, status=status.HTTP_201_CREATED)

class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        content_type_id = request.data.get('content_type_id')
        object_id = request.data.get('object_id')

        try:
            cart = Cart.objects.get(user=request.user)
            item = CartItem.objects.get(
                cart=cart,
                content_type_id=content_type_id,
                object_id=object_id
            )
            item.delete()
            return Response({'message': 'Item removed from cart.'}, status=status.HTTP_204_NO_CONTENT)
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            return Response({'error': 'Item not found in cart.'}, status=status.HTTP_404_NOT_FOUND)

class UpdateCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        content_type_id = request.data.get('content_type_id')
        object_id = request.data.get('object_id')
        new_quantity = int(request.data.get('quantity', 1))

        try:
            cart = Cart.objects.get(user=request.user)
            item = CartItem.objects.get(
                cart=cart,
                content_type_id=content_type_id,
                object_id=object_id
            )
            item.quantity = new_quantity
            item.save()
            return Response({'message': 'Cart updated.'}, status=status.HTTP_200_OK)
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            return Response({'error': 'Item not found in cart.'}, status=status.HTTP_404_NOT_FOUND)

class CartView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def get(self, request, *args, **kwargs):
        cart = self.get_object()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class DrillingMachineViewSet(viewsets.ModelViewSet):
    queryset = DrillingMachine.objects.all()
    serializer_class = DrillingMachineSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ExcavatorViewSet(viewsets.ModelViewSet):
    queryset = Excavator.objects.all()
    serializer_class = ExcavatorSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class LoaderViewSet(viewsets.ModelViewSet):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class TransportTruckViewSet(viewsets.ModelViewSet):
    queryset = TransportTruck.objects.all()
    serializer_class = TransportTruckSerializer

    def get_serializer_context(self):
        return {'request': self.request}
