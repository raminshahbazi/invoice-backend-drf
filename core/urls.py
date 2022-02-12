from django.urls import path
from core.views import ItemListAPIView

urlpatterns = [
    path('items-list', ItemListAPIView.as_view(), name='items-list')
]
