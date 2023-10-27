from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from boosts.forms import InspirationalForm
from boosts.models import Inspirational


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
            username="RegisteredUser",
            password="a_test_password",
            registration_accepted=True,
        )
        cls.user_registration_accepted_false = CustomUser.objects.create_user(
            username="UnregisteredUser",
            password="a_test_password",
            registration_accepted=False,
        )
        # Create inspirationals for testing.
        for inspirational_id in range(13):
            Inspirational.objects.create(
                author=cls.user_registration_accepted_true,
                body=f"Body for inspirational {inspirational_id}",
            )

    def test_view_redirects_to_login_if_user_is_not_authenticated(self):
        """
        View should redirect user to login view if user is not authenticated.
        """
        response = self.client.get("/boosts/inspirationals/")
        self.assertRedirects(
            response, f"{'/accounts/login/'}?next={'/boosts/inspirationals/'}"
        )

    def test_view_url_returns_200_if_user_is_authenticated(self):
        """
        View should return 200 if user is authenticated.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        """
        View should be accessible by name.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get(reverse("boosts:inspirational-list"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        View should use the correct template.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
        self.assertTemplateUsed(response, "boosts/inspirational_list.html")

    def test_view_pagination_is_ten(self):
        """
        View should paginate the list of `Inspirational`s by `10` (10).
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] == True)
        self.assertTrue(len(response.context["object_list"]) == 10)

    def test_view_returns_inspirational_objects(self):
        """
        View should return `Inspirational` objects.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("object_list" in response.context)
        self.assertTrue(len(response.context["object_list"]) == 10)
        for object in response.context["object_list"]:
            self.assertIsInstance(object, Inspirational)

    def test_view_returns_all_inspirationals(self):
        """
        View should return all `Inspirational`s.

        Page one should show 10 `Inspirational`s.
        Page two should show the 3 remaining `Inspirational`s.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response_page_one = self.client.get("/boosts/inspirationals/")
        self.assertEqual(response_page_one.status_code, 200)
        self.assertTrue("is_paginated" in response_page_one.context)
        self.assertTrue(response_page_one.context["is_paginated"] == True)
        self.assertTrue(len(response_page_one.context["object_list"]) == 10)
        response_page_two = self.client.get("/boosts/inspirationals/" + "?page=2")
        self.assertEqual(response_page_two.status_code, 200)
        self.assertTrue("is_paginated" in response_page_two.context)
        self.assertTrue(response_page_two.context["is_paginated"] == True)
        self.assertTrue(len(response_page_two.context["object_list"]) == 3)

    def test_view_for_authenticated_registration_accepted_false_user(self):
        """
        View should return 403 if user is authenticated and registration_accepted is False.
        """
        login = self.client.login(
            username="UnregisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
        self.assertEqual(response.status_code, 403)

    def test_view_for_authenticated_registration_accepted_true_user(self):
        """
        View should return 200 if user is authenticated and registration_accepted is True.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/inspirationals/")
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
            username="RegisteredUser",
            password="a_test_password",
            registration_accepted=True,
        )
        cls.user_registration_accepted_false = CustomUser.objects.create_user(
            username="UnregisteredUser",
            password="a_test_password",
            registration_accepted=False,
        )

    def test_view_uses_proper_form_class(self):
        """
        View should use the proper form class.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], InspirationalForm)

    def test_view_uses_proper_template(self):
        """
        View should use the proper template.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertTemplateUsed(response, "boosts/inspirational_form.html")

    def test_view_routes_to_proper_success_url(self):
        """
        View should route to the proper success URL.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.post(
            "/boosts/create/",
            data={
                "body": "This is a test inspirational body.",
                "author": "Test author",
            },
        )
        self.assertRedirects(response, "/boosts/inspirationals/")

    def test_view_redirects_if_user_not_logged_in(self):
        """
        View should redirect if user is not logged in.
        """
        response = self.client.get("/boosts/create/")
        self.assertTrue(response.status_code, 302)
        self.assertRedirects(response, f"{'/accounts/login/'}?next={'/boosts/create/'}")

    def test_view_returns_403_if_user_registration_accepted_false(self):
        """
        View should return 403 if user registration_accepted False.
        """
        login = self.client.login(
            username="UnregisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertEqual(response.status_code, 403)

    def test_view_returns_200_if_user_registration_accepted_true(self):
        """
        View should return 200 if user registration_accepted True.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertEqual(response.status_code, 200)

    def test_view_context_contains_page_title(self):
        """
        View context should contain page title.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        # Test that `page_title` is in `response.context`
        self.assertTrue("page_title" in response.context)
        # Test that `page_title` is equal to "Create an Inspirational"
        self.assertEqual(response.context["page_title"], "Create an Inspirational")

    def test_view_context_contains_the_site_name(self):
        """
        View context should contain the site name.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertTrue("the_site_name" in response.context)
        self.assertEqual(response.context["the_site_name"], "Boosts")

    def test_view_context_contains_hide_inspirational_create_link(self):
        """
        View context should contain hide_inspirational_create_link.
        """
        login = self.client.login(
            username="RegisteredUser",
            password="a_test_password",
        )
        response = self.client.get("/boosts/create/")
        self.assertTrue("hide_inspirational_create_link" in response.context)
        self.assertEqual(response.context["hide_inspirational_create_link"], True)

    # def test_redirect_if_not_logged_in(self):
    #     """
    #     Test that user is redirected to login page if not logged in.
    #     """
    #     response = self.client.get('/boosts/inspirationals/')
    #     self.assertRedirects(response, f"{'/accounts/login/'}?next={'/boosts/inspirationals/'}")

    # def test_logged_in_uses_correct_template(self):
    #     """
    #     Test that the correct template is used when user is logged in.
    #     """
    #     login = self.client.login(
    #         username="RegisteredUser",
    #         password="a_test_password",
    #     )
    #     response = self.client.get('/boosts/inspirationals/')
    #     self.assertEqual(
    #         str(response.context["user"]), "RegisteredUser"
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'boosts/inspirational_list.html')

    # def test_logged_in_with_correct_user(self):
    #     """
    #     Test that the correct user is logged in.
    #     """
    #     login = self.client.login(
    #         username="RegisteredUser",
    #         password="a_test_password",
    #     )
    #     response = self.client.get('/boosts/inspirationals/')
    #     self.assertEqual(
    #         str(response.context["user"]), "RegisteredUser"
    #     )

    # def test_logged_in_with_incorrect_user(self):
    #     """
    #     Test that the incorrect user is not logged in.
    #     """
    #     login = self.client.login(
    #         username="UnregisteredUser",
    #         password="a_test_password",
    #     )
    #     response = self.client.get('/boosts/inspirationals/')
    #     self.assertEqual(
    #         str(response.context["user"]), "UnregisteredUser"
    #     )

    # def test_logged_in_with_correct_user_has_correct_page_title(self):
    #     """
    #     Test that the correct page title is used when the correct user is logged in.
    #     """
    #     login = self.client.login(
    #         username="RegisteredUser",
    #         password="a_test_password",
    #     )
    #     response = self.client.get('/boosts/inspirationals/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, "Inspirational List")
