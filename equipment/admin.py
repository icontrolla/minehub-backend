from django.contrib import admin
from .models import Equipment, EquipmentCategory, DrillingMachine, Excavator, Loader, TransportTruck

admin.site.register(DrillingMachine)
admin.site.register(Excavator)
admin.site.register(Loader)
admin.site.register(TransportTruck)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_day', 'available', 'date_added')
    list_filter = ('available', 'category')
    search_fields = ('name', 'description')

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
