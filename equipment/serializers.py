from rest_framework import serializers
from .models import Equipment, DrillingMachine, Excavator, Loader, TransportTruck
from .models import Cart, CartItem
from django.contrib.contenttypes.models import ContentType

class CartItemSerializer(serializers.ModelSerializer):
    machine_name = serializers.SerializerMethodField()
    machine_price = serializers.SerializerMethodField()
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'machine_name', 'machine_price', 'quantity', 'subtotal']

    def get_machine_name(self, obj):
        return obj.machine.name if obj.machine else None

    def get_machine_price(self, obj):
        return obj.machine.price if obj.machine else None


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class DrillingMachineSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = DrillingMachine
        fields = ['id', 'name', 'description', 'price', 'image', 'availability', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class ExcavatorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Excavator
        fields = ['id', 'name', 'description', 'price', 'image', 'availability', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class LoaderSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Loader
        fields = ['id', 'name', 'description', 'price', 'image', 'availability', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


class TransportTruckSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TransportTruck
        fields = ['id', 'name', 'description', 'price', 'image', 'availability', 'created_at']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None


