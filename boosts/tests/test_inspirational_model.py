from django.test import TestCase
from django.db import models

from boosts.models import Inspirational
from accounts.models import CustomUser

A_TEST_USERNAME = 'ACustomUser'
A_TEST_INSPIRATIONAL_BODY = (
    """
    This is an Inspirational Body, here. It's a long string of text, and it
    might not be tested for length, but it's here since we have to
    provide a 'body' when creating a `Inspirational`.
    """
)


class InspirationalModelTest(TestCase):
    """
    Tests for `Inspirational` model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.

        This specific function name `setUpTestData` is required by Django.
        """
        author = CustomUser.objects.create(
            username=A_TEST_USERNAME,
        )
        Inspirational.objects.create(
            author=author,
            body=A_TEST_INSPIRATIONAL_BODY,
        )

    def test_body_max_length_attribute(self):
        """
        `Inspirational` `body` field `max_length` attribute should be 500.
        """
        inspirational = Inspirational.objects.get(id=1)
        max_length = inspirational._meta.get_field('body').max_length
        self.assertEqual(max_length, 500)

    def test_body_help_text_attribute(self):
        """
        `Inspirational` `body` field `help_text` attribute should be `Required. 500 characters or fewer.`.
        """
        inspirational = Inspirational.objects.get(id=1)
        help_text = inspirational._meta.get_field('body').help_text
        self.assertEqual(help_text, 'Required. 500 characters or fewer.')

    def test_body_verbose_name_attribute(self):
        """
        `Inspirational` `body` field `verbose_name` attribute should be `Inspirational Body Text`.
        """
        inspirational = Inspirational.objects.get(id=1)
        verbose_name = inspirational._meta.get_field('body').verbose_name
        self.assertEqual(verbose_name, 'Inspirational Body Text')

    def test_author_foreign_key(self):
        """
        `Inspirational` `author` should be a `ForeignKey` to `CustomUser`.
        """
        inspirational = Inspirational.objects.get(id=1)
        author = inspirational._meta.get_field('author').remote_field.model
        # Three ways to test the same thing:
        self.assertTrue(author is CustomUser)   # Tests identity (same object)
        self.assertIs(author, CustomUser)       # Tests identity (same object)
        self.assertEqual(author, CustomUser)    # Tests equality (same value)

    def test_author_on_delete_attribute(self):
        """
        `Inspirational` `author` field `on_delete` attribute should be `CASCADE`.
        """
        inspirational = Inspirational.objects.get(id=1)
        on_delete = inspirational._meta.get_field('author').remote_field.on_delete
        self.assertEqual(on_delete, models.CASCADE)

    def test_author_related_name(self):
        """
        `Inspirational` `author` field `related_name` attribute should be `inspirationals`.
        """
        inspirational = Inspirational.objects.get(id=1)
        related_name = inspirational._meta.get_field('author').related_query_name()
        self.assertEqual(related_name, 'inspirationals')

    def test_created_auto_now_add_attribute(self):
        """
        `Inspirational` `created` field `auto_now_add` attribute should be `True`.
        """
        inspirational = Inspirational.objects.get(id=1)
        auto_now_add = inspirational._meta.get_field('created').auto_now_add
        self.assertTrue(auto_now_add)

