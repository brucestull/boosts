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
        `body` field max_length should be 500.
        """
        inspirational = Inspirational.objects.get(id=1)
        max_length = inspirational._meta.get_field('body').max_length
        self.assertEqual(max_length, 500)

    def test_body_help_text_attribute(self):
        """
        `body` field help_text should be `Required. 500 characters or fewer.`
        """
        inspirational = Inspirational.objects.get(id=1)
        help_text = inspirational._meta.get_field('body').help_text
        self.assertEqual(help_text, 'Required. 500 characters or fewer.')

    def test_body_verbose_name_attribute(self):
        """
        `body` field `verbose_name` should be `Inspirational Body Text`.
        """
        inspirational = Inspirational.objects.get(id=1)
        field_label = inspirational._meta.get_field('body').verbose_name
        self.assertEqual(field_label, 'Inspirational Body Text')

    def test_body_blank_attribute(self):
        """
        `body` field blank should be False.
        """
        inspirational = Inspirational.objects.get(id=1)
        blank = inspirational._meta.get_field('body').blank
        self.assertEqual(blank, False)

    def test_body_null_attribute(self):
        """
        `body` field null should be False.
        """
        inspirational = Inspirational.objects.get(id=1)
        null = inspirational._meta.get_field('body').null
        self.assertEqual(null, False)

    def test_author_foreign_key(self):
        """
        `author` field should be a ForeignKey to `CustomUser`.
        """
        inspirational = Inspirational.objects.get(id=1)
        field = inspirational._meta.get_field('author')
        self.assertEqual(field.remote_field.model, CustomUser)

    # How best to test `on_delete` attribute?
    def test_author_on_delete_attribute(self):
        """
        `author` field `on_delete` attribute should be `models.CASCADE`.
        """
        inspirational = Inspirational.objects.get(id=1)
        on_delete = inspirational._meta.get_field('author').remote_field.on_delete
        self.assertIsInstance(on_delete, models.CASCADE.__class__)

    def test_author_related_name_attribute(self):
        """
        `author` `related_name` attribute should be `inspirationals`.
        """
        inspirational = Inspirational.objects.get(id=1)
        related_name = inspirational._meta.get_field('author').related_query_name()
        self.assertEqual(related_name, 'inspirationals')

    def test_created_auto_now_add_attribute(self):
        """
        `created` field `auto_now_add` attribute should be True.
        """
        inspirational = Inspirational.objects.get(id=1)
        auto_now_add = inspirational._meta.get_field('created').auto_now_add
        self.assertEqual(auto_now_add, True)

    def test_dunder_str(self):
        """
        `__str__` method should return a string in the format:
        `author.username : id - body[:24]`
        """
        inspirational = Inspirational.objects.get(id=1)
        expected_str = (
            f'{inspirational.author.username} : {inspirational.id} - '
            f'{inspirational.body[:24]}'
        )
        self.assertEqual(str(inspirational), expected_str)
