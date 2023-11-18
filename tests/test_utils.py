from django.test import TestCase
from utils import get_database_config_variables


class GetDatabaseConfigVariablesTest(TestCase):
    def test_valid_database_url(self):
        url = "postgres://user:password@host:5432/dbname"
        expected_output = {
            "DATABASE_USER": "user",
            "DATABASE_PASSWORD": "password",
            "DATABASE_HOST": "host",
            "DATABASE_PORT": "5432",
            "DATABASE_NAME": "dbname",
        }
        self.assertEqual(get_database_config_variables(url), expected_output)

    # def test_invalid_database_url(self):
    #     url = "invalid_url"
    #     # Depending on how you want to handle invalid input,
    #     # this could raise an error or return an empty dict or None.
    #     with self.assertRaises(ValueError):  # or any appropriate exception
    #         get_database_config_variables(url)

    # You can add more tests for different variations or edge cases
