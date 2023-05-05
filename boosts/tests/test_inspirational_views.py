from django.test import TestCase
from django.urls import reverse

from boosts.models import Inspirational
from boosts.forms import InspirationalForm
from accounts.models import CustomUser

THE_SITE_NAME = "Boosts"

USERNAME_REGISTRATION_ACCEPTED_TRUE = "RegisteredUser"
USERNAME_REGISTRATION_ACCEPTED_FALSE = "UnregisteredUser"
PASSWORD_FOR_TESTING = "a_test_password"

LOGIN_URL = "/accounts/login/"

NUMBER_OF_INSPIRATIONALS = 13
NUMBER_OF_INSPIRATIONALS_PER_PAGE = 10

INSPIRATIONAL_LIST_URL = "/boosts/inspirationals/"
INSPIRATIONAL_LIST_VIEW_NAME = "boosts:inspirational-list"
INSPIRATIONAL_LIST_TEMPLATE = "boosts/inspirational_list.html"
INSPIRATIONAL_LIST_PAGE_TITLE = "Inspirational List"

INSPIRATIONAL_CREATE_URL = "/boosts/create/"
INSPIRATIONAL_CREATE_VIEW_NAME = "boosts:inspirational-create"
INSPIRATIONAL_CREATE_TEMPLATE = "boosts/inspirational_form.html"
INSPIRATIONAL_CREATE_PAGE_TITLE = "Create an Inspirational"

INSPIRATIONAL_BODY = "This is a test inspirational body."


class InspirationalListViewTest(TestCase):
    """
    Test the InspirationalListView.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create `CustomUser`s and `Inspirational`s for testing.
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
        # Create inspirationals for testing.
        for inspirational_id in range(NUMBER_OF_INSPIRATIONALS):
            Inspirational.objects.create(
                author=cls.user_registration_accepted_true,
                body=f"Body for inspirational {inspirational_id}",
            )

    def test_view_redirects_to_login_if_user_is_not_authenticated(self):
        """
        View should redirect user to login view if user is not authenticated.
        """
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertRedirects(response, f"{LOGIN_URL}?next={INSPIRATIONAL_LIST_URL}")

    def test_view_url_returns_200_if_user_is_authenticated(self):
        """
        View should return 200 if user is authenticated.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        """
        View should be accessible by name.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(reverse(INSPIRATIONAL_LIST_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        View should use the correct template.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertTemplateUsed(response, INSPIRATIONAL_LIST_TEMPLATE)

    def test_view_pagination_is_ten(self):
        """
        View should paginate the list of `Inspirational`s by `NUMBER_OF_INSPIRATIONALS_PER_PAGE` (10).
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] == True)
        self.assertTrue(len(response.context["object_list"]) == NUMBER_OF_INSPIRATIONALS_PER_PAGE)

    def test_view_returns_inspirational_objects(self):
        """
        View should return `Inspirational` objects.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("object_list" in response.context)
        self.assertTrue(len(response.context["object_list"]) == NUMBER_OF_INSPIRATIONALS_PER_PAGE)
        for object in response.context["object_list"]:
            self.assertIsInstance(object, Inspirational)

    def test_view_returns_all_inspirationals(self):
        """
        View should return all `Inspirational`s.

        Page one should show 10 `Inspirational`s.
        Page two should show the 3 remaining `Inspirational`s.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response_page_one = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response_page_one.status_code, 200)
        self.assertTrue("is_paginated" in response_page_one.context)
        self.assertTrue(response_page_one.context["is_paginated"] == True)
        self.assertTrue(len(response_page_one.context["object_list"]) == NUMBER_OF_INSPIRATIONALS_PER_PAGE)
        response_page_two = self.client.get(INSPIRATIONAL_LIST_URL + "?page=2")
        self.assertEqual(response_page_two.status_code, 200)
        self.assertTrue("is_paginated" in response_page_two.context)
        self.assertTrue(response_page_two.context["is_paginated"] == True)
        self.assertTrue(len(response_page_two.context["object_list"]) == 3)

    def test_view_for_authenticated_registration_accepted_false_user(self):
        """
        View should return 403 if user is authenticated and registration_accepted is False.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 403)

    def test_view_for_authenticated_registration_accepted_true_user(self):
        """
        View should return 200 if user is authenticated and registration_accepted is True.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_LIST_URL)
        self.assertEqual(response.status_code, 200)

class InspirationalCreateViewTest(TestCase):
    """
    Test `InspirationalCreateView`.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create test data.
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

    def test_view_uses_proper_form_class(self):
        """
        View should use the proper form class.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], InspirationalForm)

    def test_view_uses_proper_template(self):
        """
        View should use the proper template.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertTemplateUsed(response, INSPIRATIONAL_CREATE_TEMPLATE)

    def test_view_routes_to_proper_success_url(self):
        """
        View should route to the proper success URL.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.post(
            INSPIRATIONAL_CREATE_URL,
            data={
                "body": INSPIRATIONAL_BODY,
                "author": "Test author",
            },
        )
        self.assertRedirects(response, INSPIRATIONAL_LIST_URL)

    def test_view_redirects_if_user_not_logged_in(self):
        """
        View should redirect if user is not logged in.
        """
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, f"{LOGIN_URL}?next={INSPIRATIONAL_CREATE_URL}")

    def test_view_returns_403_if_user_registration_accepted_false(self):
        """
        View should return 403 if user registration_accepted False.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertEqual(response.status_code, 403)

    def test_view_returns_200_if_user_registration_accepted_true(self):
        """
        View should return 200 if user registration_accepted True.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_view_context_contains_page_title(self):
        """
        View context should contain page title.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertTrue("page_title" in response.context)
        self.assertEqual(response.context["page_title"], INSPIRATIONAL_CREATE_PAGE_TITLE)

    def test_view_context_contains_the_site_name(self):
        """
        View context should contain the site name.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertTrue("the_site_name" in response.context)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)

    def test_view_context_contains_hide_inspirational_create_link(self):
        """
        View context should contain hide_inspirational_create_link.
        """
        login = self.client.login(
            username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
            password=PASSWORD_FOR_TESTING,
        )
        response = self.client.get(INSPIRATIONAL_CREATE_URL)
        self.assertTrue("hide_inspirational_create_link" in response.context)
        self.assertEqual(response.context["hide_inspirational_create_link"], True)




    # def test_redirect_if_not_logged_in(self):
    #     """
    #     Test that user is redirected to login page if not logged in.
    #     """
    #     response = self.client.get(INSPIRATIONAL_LIST_URL)
    #     self.assertRedirects(response, f"{LOGIN_URL}?next={INSPIRATIONAL_LIST_URL}")

    # def test_logged_in_uses_correct_template(self):
    #     """
    #     Test that the correct template is used when user is logged in.
    #     """
    #     login = self.client.login(
    #         username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
    #         password=PASSWORD_FOR_TESTING,
    #     )
    #     response = self.client.get(INSPIRATIONAL_LIST_URL)
    #     self.assertEqual(
    #         str(response.context["user"]), USERNAME_REGISTRATION_ACCEPTED_TRUE
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, INSPIRATIONAL_LIST_TEMPLATE)

    # def test_logged_in_with_correct_user(self):
    #     """
    #     Test that the correct user is logged in.
    #     """
    #     login = self.client.login(
    #         username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
    #         password=PASSWORD_FOR_TESTING,
    #     )
    #     response = self.client.get(INSPIRATIONAL_LIST_URL)
    #     self.assertEqual(
    #         str(response.context["user"]), USERNAME_REGISTRATION_ACCEPTED_TRUE
    #     )

    # def test_logged_in_with_incorrect_user(self):
    #     """
    #     Test that the incorrect user is not logged in.
    #     """
    #     login = self.client.login(
    #         username=USERNAME_REGISTRATION_ACCEPTED_FALSE,
    #         password=PASSWORD_FOR_TESTING,
    #     )
    #     response = self.client.get(INSPIRATIONAL_LIST_URL)
    #     self.assertEqual(
    #         str(response.context["user"]), USERNAME_REGISTRATION_ACCEPTED_FALSE
    #     )

    # def test_logged_in_with_correct_user_has_correct_page_title(self):
    #     """
    #     Test that the correct page title is used when the correct user is logged in.
    #     """
    #     login = self.client.login(
    #         username=USERNAME_REGISTRATION_ACCEPTED_TRUE,
    #         password=PASSWORD_FOR_TESTING,
    #     )
    #     response = self.client.get(INSPIRATIONAL_LIST_URL)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, INSPIRATIONAL_LIST_PAGE_TITLE)
