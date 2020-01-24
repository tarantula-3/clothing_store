from django.contrib import admin
from .models import ClothesType, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'type',
    )


admin.site.register(ClothesType)
admin.site.register(Item, ItemAdmin)