from datetime import time

from django.db import IntegrityError
from django.test import TestCase

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
