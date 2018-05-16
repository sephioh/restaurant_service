from datetime import time

from behave import given, when, then
from model_mommy import mommy

from restaurants.models import Restaurant


@given('there is a restaurant called {name}')
def step_impl(context, name):
    mommy.make(
        Restaurant,
        name=name,
        opens_at=time(hour=10),
        closes_at=time(hour=22)
    )


@given('there is a restaurant with a {restaurant_id} id')
def step_impl(context, restaurant_id):
    mommy.make(
        Restaurant,
        id=restaurant_id,
        name="Some restaurant",
        opens_at=time(hour=10),
        closes_at=time(hour=22)
    )


@when('we make a HTTP GET request to {path}')
def step_impl(context, path):
    context.response = context.test.client.get(path=path)


@when('we make a HTTP POST request to {path}')
def step_impl(context, path):
    restaurant_name = 'A New Restaurant'
    restaurant_opens_at = '12:00:00'
    restaurant_closes_at = '23:00:00'

    context.response = context.test.client.post(
        path=path,
        data={
            'name': restaurant_name,
            'opens_at': restaurant_opens_at,
            'closes_at': restaurant_closes_at,
        }
    )


@when('we make a HTTP DELETE request to {path}')
def step_impl(context, path):
    context.response = context.test.client.delete(
        path=path,
    )


@then('this restaurant should be listed on the response')
def step_impl(context):
    [restaurant] = Restaurant.objects.all()

    context.test.assertEqual(context.response.data[0]['id'], restaurant.id)
    context.test.assertEqual(context.response.data[0]['name'], restaurant.name)


@then('this restaurant should be on the response')
def step_impl(context):
    [restaurant] = Restaurant.objects.all()

    context.test.assertEqual(context.response.data['id'], restaurant.id)
    context.test.assertEqual(context.response.data['name'], restaurant.name)


@then('this restaurant should be created')
def step_impl(context):
    [restaurant] = Restaurant.objects.all()

    context.test.assertEqual(context.response.data['id'], restaurant.id)
    context.test.assertEqual(context.response.data['name'], restaurant.name)


@then('the restaurant with a id {restaurant_id} should be deleted')
def step_impl(context, restaurant_id):
    restaurant_exists = Restaurant.objects.filter(id=restaurant_id).exists()

    context.test.assertFalse(restaurant_exists, "Restaurant should be deleted but still exists!")
