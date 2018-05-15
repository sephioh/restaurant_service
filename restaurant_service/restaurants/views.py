from rest_framework.generics import ListCreateAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantListView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
