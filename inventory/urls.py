# inventory/urls.py
from django.urls import path
from .views import ItemList, ItemDetail

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<int:item_id>/', ItemDetail.as_view(), name='item-detail'),
]
