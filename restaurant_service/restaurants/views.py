from rest_framework.generics import ListAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
