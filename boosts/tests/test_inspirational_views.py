from django.test import TestCase
from django.urls import reverse

from boosts.models import Inspirational
from accounts.models import CustomUser

SERVER_ROOT = "http://localhost:8000"

A_CUSTOM_USER_USERNAME = 'ACustomUser'

INSPIRATIONAL_LIST_URL = "/boosts/inspirationals/"
INSPIRATIONAL_LIST_VIEW_NAME = "boosts:inspirational-list"
INSPIRATIONAL_LIST_TEMPLATE = "boosts/inspirational_list.html"

PAGE_TITLE_INSPIRATIONAL_LIST = "Inspirational List"

NUMBER_OF_INSPIRATIONALS = 13



class InspirationalListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """

        # Create a CustomUser object:
        custom_user = CustomUser.objects.create(
            username=A_CUSTOM_USER_USERNAME,
        )

        for inspirational_id in range(NUMBER_OF_INSPIRATIONALS):
            Inspirational.objects.create(
                author=custom_user,
                body=f'This is a body, {inspirational_id}, here.',
            )

    def test_view_url_exists_at_desired_location(self):
        """
        URL 'INSPIRATIONAL_LIST_URL' should exist.
        """
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        Test that the view URL is accessible by name.
        """
        response = self.client.get(reverse(INSPIRATIONAL_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test that the view uses the correct template.
        """
        response = self.client.get(reverse(INSPIRATIONAL_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, INSPIRATIONAL_LIST_TEMPLATE)

    def test_pagination_is_ten(self):
        """
        Test that the view uses pagination, and that there are ten
        Inspirational objects per page.
        """
        response = self.client.get(reverse(INSPIRATIONAL_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['inspirational_list']) == 10)

    def test_lists_all_inspirationals(self):
        """
        Test that all Inspirational objects are listed on the page.
        """
        # Get second page and confirm it has (exactly) remaining 3 items
        # /boosts/inspirationals/?page=2
        url = SERVER_ROOT + INSPIRATIONAL_LIST_URL + '?page=2'
        response = self.client.get(url)
        # response = self.client.get(reverse(INSPIRATIONAL_LIST_VIEW_NAME) + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['inspirational_list']) == 3)
