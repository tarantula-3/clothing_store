from django.shortcuts import render
from .models import Item, ClothesType


def index(request):
    return render(request, 'clothing/index.html')


def all_product(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'clothing/all_products.html', context=context)
