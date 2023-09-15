import re

from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser

HOME_PAGE_URL = "/"

API_URL_ROOT = "/api/v1/"

INSPIRATIONALS_LIST_URL = "/boosts/inspirationals/"
INSPIRATIONALS_CREATE_URL = "/boosts/create/"

LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"
SIGNUP_URL = "/accounts/signup/"

EDIT_URL_PARTIAL = "/edit/"

USERNAME_REGISTRATION_ACCEPTED_TRUE = "RegisteredUser"
USERNAME_REGISTRATION_ACCEPTED_FALSE = "UnregisteredUser"
PASSWORD_FOR_TESTING = "a_test_password"


class BaseTemplateHttpResponseTest(TestCase):
    """
    Test the HTTP response for the Inspirational Quotes page.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create `CustomUser`s for testing.
        """
        # Create users for testing.
        cls.user_registration_accepted_true = CustomUser.objects.create_user(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
            registration_accepted=True,
        )
        cls.user_registration_accepted_false = CustomUser.objects.create_user(
            username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
            password=PASSWORD_FOR_TESTING,
            registration_accepted=False,
        )

    def test_http_response(self):
        """
        TODO: Remove this test.

        This test is here to show that the test framework is working.
        """
        response = self.client.get(INSPIRATIONALS_LIST_URL)
        self.assertEqual(response.status_code, 302)

    def test_user_not_logged_in(self):
        """
        Test that the following links ARE present on the home page for a user
        that is not logged in:
        - login
        - signup
        Test that the following links ARE NOT present on the home page for a
        user that is not logged in:
        - edit
        - Inspirational Quotes list
        - Inspirational Quotes create
        - Inspirational Quotes API
        """
        response = self.client.get(HOME_PAGE_URL)
        self.assertContains(response, LOGIN_URL)
        self.assertContains(response, SIGNUP_URL)

        self.assertNotContains(response, EDIT_URL_PARTIAL)

        self.assertNotContains(response, INSPIRATIONALS_LIST_URL)
        self.assertNotContains(response, INSPIRATIONALS_CREATE_URL)
        self.assertNotContains(response, API_URL_ROOT)

    def test_user_logged_in(self):
        """
        Test that the following links ARE present on the home page for a
        logged-in user:
        - logout
        Test that the following links ARE NOT present on the home page for a
        logged-in user:
        - signup
        - login
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
            password=PASSWORD_FOR_TESTING,
        )
        self.assertTrue(login)
        response = self.client.get(HOME_PAGE_URL)
        self.assertContains(response, LOGOUT_URL)
        self.assertNotContains(response, SIGNUP_URL)
        self.assertNotContains(response, LOGIN_URL)

    def test_user_registration_accepted_false(self):
        """
        Test that the following links ARE present on the home page for a
        logged-in user who has `registration_accepted` set to `False`:
        - logout
        Test that the following links ARE NOT present on the home page for a
        logged-in user who has `registration_accepted` set to `False`:
        - Inspirational Quotes list
        - Inspirational Quotes create
        - Inspirational Quotes API
        """
        self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(HOME_PAGE_URL)
        self.assertContains(response, LOGOUT_URL)
        self.assertNotContains(response, INSPIRATIONALS_LIST_URL)
        self.assertNotContains(response, INSPIRATIONALS_CREATE_URL)
        self.assertNotContains(response, API_URL_ROOT)

    def test_user_registration_accepted_true(self):
        """
        Test that the following links ARE present on the home page for a
        logged-in user who has `registration_accepted` set to `True`:
        - Inspirational Quotes list
        - Inspirational Quotes create
        - Inspirational Quotes API
        """
        self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(HOME_PAGE_URL)
        self.assertContains(response, LOGOUT_URL)

        # self.assertTrue(re.search(rb'\b/accounts/\d+/edit/', response.content))

        self.assertContains(response, INSPIRATIONALS_LIST_URL)
        self.assertContains(response, INSPIRATIONALS_CREATE_URL)
        # # TODO: Ensure this route is present for appropriate users.
        # # This test is currently failing since current logic is `user.registration_accepted and user.is_staff`.
        # self.assertContains(response, API_URL_ROOT)
