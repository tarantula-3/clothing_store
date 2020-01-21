from django.shortcuts import render
from .models import Item, ClothesType


def index(request):
    return render(request, 'clothing/index.html')
