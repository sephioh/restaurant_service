from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListCreateAPIView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantRetrieveAPIView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
