from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListCreateAPIView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantRetrieveUpdateDestroyAPIViewAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
