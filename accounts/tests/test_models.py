from django.test import TestCase
from django.db import models

from accounts.models import CustomUser

A_TEST_USERNAME = "ACustomUser"


class CustomUserModelTest(TestCase):
    """
    Tests for `CustomUser` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        cls.user = CustomUser.objects.create(
            username=A_TEST_USERNAME,
        )

    def test_has_registration_accepted_field(self):
        """
        `CustomUser` model should have `registration_accepted` field.
        """
        self.assertTrue(hasattr(CustomUser, "registration_accepted"))

    def test_registration_accepted_field_is_boolean_field(self):
        """
        `CustomUser` model `registration_accepted` field should be `BooleanField`.
        """
        user = CustomUser.objects.get(id=1)
        registration_accepted_field = user._meta.get_field("registration_accepted")
        self.assertIsInstance(registration_accepted_field, models.BooleanField)

    def test_registration_accepted_default_attribute_is_false(self):
        """
        `CustomUser` model `registration_accepted` field `default` attribute should be
        `False`.
        """
        user = CustomUser.objects.get(id=1)
        registration_accepted_field = user._meta.get_field("registration_accepted")
        self.assertFalse(registration_accepted_field.default)

    def test_dunder_string_method(self):
        """
        `CustomUser` model `__str__` method should return `username`.
        """
        user = CustomUser.objects.get(id=1)
        self.assertEqual(user.__str__(), user.username)
