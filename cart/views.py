from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer


class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.prefetch_related("items").all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.prefetch_related("items").all()
    serializer_class = CartSerializer
