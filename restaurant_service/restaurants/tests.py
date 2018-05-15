from datetime import time

from django.db import IntegrityError
from django.test import TestCase
from rest_framework.status import HTTP_200_OK

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


class TestRestaurantListView(TestCase):
    def test_returns_200_ok(self):
        response = self.client.get('/api/restaurants/')
        self.assertEqual(HTTP_200_OK, response.status_code)
