from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.prefetch_related("items").all()
    serializer_class = OrderSerializer
