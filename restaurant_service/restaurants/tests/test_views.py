import json
from datetime import time

from django.test import TestCase
from model_mommy import mommy
from rest_framework import status

from restaurants.models import Restaurant


class TestRestaurantListCreateAPIView(TestCase):
    def test_get_restaurants_returns_200_ok(self):
        response = self.client.get('/api/restaurants/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_restaurants_returns_201_created(self):
        data = dict(
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )
        response = self.client.post('/api/restaurants/', data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class TestRestaurantRetrieveUpdateDestroyAPIViewAPIView(TestCase):
    def test_retrieve_returns_200_ok(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        response = self.client.get('/api/restaurant/{0}'.format(restaurant.id))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_retrieve_non_existent_restaurant_returns_404_not_found(self):
        non_existent_restaurant_id = 1111

        response = self.client.get('/api/restaurant/{0}'.format(non_existent_restaurant_id))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_delete_returns_204_no_content(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        response = self.client.delete('/api/restaurant/{0}'.format(restaurant.id))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_non_existent_restaurant_returns_404_not_found(self):
        non_existent_restaurant_id = 1111
        response = self.client.delete('/api/restaurant/{0}'.format(non_existent_restaurant_id))

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_put_returns_200_ok(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        data = {
            'id': restaurant.id,
            'name': 'The New Incredible Restaurant',
            'opens_at': '10:00',
            'closes_at': '14:00'
        }

        response = self.client.put(
            path='/api/restaurant/{0}'.format(restaurant.id),
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_put_with_missing_data_returns_400_bad_request(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        data = {
            'id': restaurant.id,
            'name': 'The New Incredible Restaurant',
        }

        response = self.client.put(
            path='/api/restaurant/{0}'.format(restaurant.id),
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_patch_returns_200_ok(self):
        restaurant = mommy.make(
            Restaurant,
            name="The Incredible Restaurant",
            opens_at=time(hour=10),
            closes_at=time(hour=22)
        )

        data = {
            'opens_at': '09:00',
        }

        response = self.client.patch(
            path='/api/restaurant/{0}'.format(restaurant.id),
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
