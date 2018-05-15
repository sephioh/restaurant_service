from datetime import time

from django.db import IntegrityError
from django.test import TestCase
from model_mommy import mommy
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from restaurants.models import Restaurant


class TestRestaurantModel(TestCase):
    def test_create_a_restaurant(self):
        Restaurant.objects.create(
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        self.assertEqual(1, Restaurant.objects.count())

    def test_restaurants_must_have_a_name(self):
        with self.assertRaises(IntegrityError):
            Restaurant.objects.create(
                opens_at=time(hour=10),
                closes_at=time(hour=22)
            )

    def test_restaurants_must_have_a_opening_time(self):
        with self.assertRaises(IntegrityError):
            Restaurant.objects.create(
                name="The Incredible Restaurant",
                closes_at=time(hour=22)
            )

    def test_restaurants_must_have_a_closing_time(self):
        with self.assertRaises(IntegrityError):
            Restaurant.objects.create(
                name="The Incredible Restaurant",
                opens_at=time(hour=10),
            )


class TestRestaurantListCreateAPIView(TestCase):
    def test_get_restaurants_returns_200_ok(self):
        response = self.client.get('/api/restaurants/')
        self.assertEqual(HTTP_200_OK, response.status_code)

    def test_create_restaurants_returns_201_created(self):
        data = dict(
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )
        response = self.client.post('/api/restaurants/', data=data)
        self.assertEqual(HTTP_201_CREATED, response.status_code)


class TestRestaurantRetrieveAPIView(TestCase):
    def test_returns_200_ok(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        response = self.client.get('/api/restaurant/{0}'.format(restaurant.id))
        self.assertEqual(HTTP_200_OK, response.status_code)
