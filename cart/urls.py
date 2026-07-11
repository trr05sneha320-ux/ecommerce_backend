from django.urls import path
from .views import CartList, CartDetail

urlpatterns = [
    path('', CartList.as_view(), name='cart-list'),
    path('<int:pk>/', CartDetail.as_view(), name='cart-detail'),
]