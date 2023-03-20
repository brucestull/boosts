from django.test import TestCase
from django.urls import reverse_lazy
from django.urls import reverse

from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm

A_TEST_USERNAME = "ACustomUser"
A_TEST_PASSWORD = "a_test_password"
A_TEST_FIRST_NAME = "A"

A_SECOND_TEST_USERNAME = "ASecondCustomUser"
A_SECOND_TEST_PASSWORD = "a_second_test_password"

THE_SITE_NAME = "Boosts"

SIGN_UP_VIEW_URL = "/accounts/signup/"
SIGN_UP_VIEW_NAME = "signup"
SIGN_UP_TEMPLATE = "registration/signup.html"

CUSTOM_LOGIN_VIEW_URL = "/accounts/login/"
CUSTOM_LOGIN_VIEW_NAME = "login"
# Django provides a default login view with a default template location so we don't need to specify it.
# CUSTOM_LOGIN_VIEW_TEMPLATE = "registration/login.html"

USER_UPDATE_VIEW_URL = "/accounts/1/edit/"
USER_UPDATE_VIEW_NAME = "edit-profile"
USER_UPDATE_VIEW_TEMPLATE = "registration/update.html"


class SignUpViewTest(TestCase):
    """
    Tests for `SignUpView` view.
    """

    def test_url_exists_at_desired_location(self):
        """
        `CustomUser` sign up view should be accessible at `/accounts/signup/`.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        `CustomUser` sign up view should be accessible by name.
        """
        response = self.client.get(reverse(SIGN_UP_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_form(self):
        """
        `CustomUser` sign up view should use `CustomUserCreationForm`.
        """
        response = self.client.get(reverse(SIGN_UP_VIEW_NAME))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertEqual(
            response.context["form"].__class__.__name__, "CustomUserCreationForm"
        )

    def test_redirects_to_correct_view_on_success(self):
        """
        `CustomUser` sign up view should redirect to the `login` view on success.
        """
        response = self.client.post(
            reverse(SIGN_UP_VIEW_NAME),
            {
                "username": A_TEST_USERNAME,
                "password1": A_TEST_PASSWORD,
                "password2": A_TEST_PASSWORD,
            },
        )
        self.assertRedirects(
            response,
            CUSTOM_LOGIN_VIEW_URL,
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_uses_correct_template(self):
        """
        `CustomUser` sign up view should use `registration/signup.html` template.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, SIGN_UP_TEMPLATE)

    def test_has_the_site_name_in_context(self):
        """
        `CustomUser` sign up view should have `the_site_name` in the context.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("the_site_name", response.context)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)

    def test_has_hide_signup_link_in_context(self):
        """
        `CustomUser` sign up view should have `hide_signup_link` in the context.
        """
        response = self.client.get(SIGN_UP_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("hide_signup_link", response.context)
        self.assertTrue(response.context["hide_signup_link"])


class CustomLoginViewTest(TestCase):
    """
    Tests for `CustomLoginView` view.
    """

    def test_url_exists_at_desired_location(self):
        """
        `CustomUser` login view should be accessible at `/accounts/login/`.
        """
        response = self.client.get(CUSTOM_LOGIN_VIEW_URL)
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        """
        `CustomUser` login view should be accessible by name.
        """
        response = self.client.get(reverse(CUSTOM_LOGIN_VIEW_NAME))
        self.assertEqual(response.status_code, 200)

    def test_has_the_site_name_in_context(self):
        """
        `CustomUser` login view should have `the_site_name` in the context.
        """
        response = self.client.get(CUSTOM_LOGIN_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("the_site_name", response.context)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)

    def test_has_hide_login_link_in_context(self):
        """
        `CustomUser` login view should have `hide_login_link` in the context.
        """
        response = self.client.get(CUSTOM_LOGIN_VIEW_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("hide_login_link", response.context)
        self.assertTrue(response.context["hide_login_link"])


class UserUpdateViewTest(TestCase):
    """
    Tests for `UserUpdateView` view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Create a test user.
        """
        cls.a_test_user = CustomUser.objects.create_user(
            username=A_TEST_USERNAME,
            password=A_TEST_PASSWORD,
        )
        pass

    def test_url_redirects_for_non_authenticated_user(self):
        """
        `CustomUser` update view should redirect to the `login` view for non-authenticated user.
        """
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertRedirects(
            response,
            CUSTOM_LOGIN_VIEW_URL + "?next=" + USER_UPDATE_VIEW_URL,
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_url_exists_for_authenticated_user(self):
        """
        `CustomUser` update view should be accessible at `/accounts/<user.pk>/edit/`.
        """

        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name_for_authenticated_user(self):
        """
        `CustomUser` update view should be accessible by name.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)

    # TODO: test for 404 if user is not found
    # TODO: test for 404 if user is not the same as the logged in user

    ####################################################################
    # TODO: Decide which of these two tests to keep.
    # This is testing the `get_object` method of the `UserUpdateView` view.
    def test_context_object_is_current_user(self):
        """
        `CustomUser` update view should use `CustomUser` model.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["object"], self.a_test_user)

    def test_object_is_custom_user_instance(self):
        """
        `CustomUser` update view should use `CustomUser` model.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["object"], CustomUser)
    ####################################################################

    def test_uses_correct_form_class(self):
        """
        `CustomUser` update view should use `CustomUserUpdateForm`.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], CustomUserChangeForm)

    # TODO: Determine if there is a better way to test this.
    def test_redirects_to_correct_success_url(self):
        """
        `CustomUser` update view should redirect to the `home` view on success.
        """
        # login = self.client.login(
        #     username=self.a_test_user.username,
        #     password=A_TEST_PASSWORD,
        # )
        # self.assertTrue(login)
        # response = self.client.post(
        #     reverse(
        #         USER_UPDATE_VIEW_NAME,
        #         kwargs={"pk": self.a_test_user.pk},
        #     ),
        #     data={
        #         "first_name": A_TEST_FIRST_NAME,
        #     },
        # )
        # self.assertRedirects(
        #     response,
        #     reverse("home"),
        #     status_code=302,
        #     target_status_code=200,
        # )
        pass

    def test_uses_correct_template(self):
        """
        `CustomUser` update view should use `user_update.html` template.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            USER_UPDATE_VIEW_URL,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, USER_UPDATE_VIEW_TEMPLATE)

    def test_has_the_site_name_in_context(self):
        """
        `CustomUser` update view should have `the_site_name` in the context.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("the_site_name", response.context)
        self.assertEqual(response.context["the_site_name"], THE_SITE_NAME)

    def test_has_hide_edit_profile_link_in_context(self):
        """
        `CustomUser` update view should have `hide_edit_profile_link` in the context.
        """
        login = self.client.login(
            username=self.a_test_user.username,
            password=A_TEST_PASSWORD,
        )
        self.assertTrue(login)
        response = self.client.get(
            reverse(
                USER_UPDATE_VIEW_NAME,
                kwargs={"pk": self.a_test_user.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("hide_edit_profile_link", response.context)
        self.assertTrue(response.context["hide_edit_profile_link"])


# login = self.client.login(
#     username=A_TEST_USERNAME,
#     password=A_TEST_PASSWORD,
# )
# self.assertTrue(login)
# response = self.client.get(USER_UPDATE_VIEW_URL)
# self.assertEqual(response.status_code, 200)

# a_second_test_user = CustomUser.objects.create_user(
#     username=A_SECOND_TEST_USERNAME,
#     password=A_SECOND_TEST_PASSWORD,
# )
# login = self.client.login(username=A_SECOND_TEST_USERNAME, password=A_SECOND_TEST_PASSWORD)
# self.assertTrue(login)
# response = self.client.get(reverse(USER_UPDATE_VIEW_NAME, kwargs={"pk": a_second_test_user.pk}))
# self.assertEqual(response.status_code, 200)
