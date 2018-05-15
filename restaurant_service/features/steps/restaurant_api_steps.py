from datetime import time

from behave import given, when, then
from model_mommy import mommy

from restaurants.models import Restaurant


@given('there is a restaurant')
def step_impl(context):
    mommy.make(
        Restaurant,
        name="The Incredible Restaurant",
        opens_at=time(hour=10),
        closes_at=time(hour=22)
    )


@when('we make a HTTP GET request to {path}')
def step_impl(context, path):
    context.response = context.test.client.get(path)


@then('this restaurant should be listed on the response')
def step_impl(context):
    [restaurant] = Restaurant.objects.all()
    context.test.assertEqual(context.response.data[0]['id'], restaurant.id)
    context.test.assertEqual(context.response.data[0]['name'], restaurant.name)
