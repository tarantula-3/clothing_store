from django.urls import path
from . import views


app_name = 'clothing'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_products/', views.all_product, name='all_products'),
]