# boosts / tests / test_tasks.py
# from unittest.mock import patch
from django.test import TestCase
from boosts.tasks import send_inspirational_to_beastie
from unittest import mock


# class SendInspirationalToBeastieTest(TestCase):
#     @patch("django.core.mail.send_mail")
#     def test_send_inspirational_to_beastie(self, mock_send_mail):
#         # Set up the data for the test
#         user_username = "user123"
#         user_email = "user@example.com"
#         user_beastie_email = "beastie@example.com"
#         user_beastie_username = "beastie123"
#         message = "Keep up the great work!"

#         # Call the task
#         send_inspirational_to_beastie.delay(
#             user_username,
#             user_email,
#             user_beastie_email,
#             user_beastie_username,
#             message,
#         )

#         # Assert send_mail was called twice
#         self.assertEqual(mock_send_mail.call_count, 2)

#         # Check the calls to send_mail with the expected data
#         beastie_email_call = mock_send_mail.call_args_list[0]
#         user_email_call = mock_send_mail.call_args_list[1]

#         # Assert the details of the first call (to the Beastie's email)
#         self.assertEqual(
#             beastie_email_call[1]["subject"],
#             f"Inspirational Quote from your Beastie: {user_username}",
#         )
#         self.assertEqual(beastie_email_call[1]["message"], message)
#         self.assertEqual(beastie_email_call[1]["from_email"], user_email)
#         self.assertEqual(
#             beastie_email_call[1]["recipient_list"], [user_beastie_email]
#         )  # noqa: E501

#         # Assert the details of the second call (to the user's email)
#         self.assertEqual(
#             user_email_call[1]["subject"],
#             f"You Sent an Inspirational Quote to your Beastie: {user_beastie_username}",  # noqa: E501
#         )
#         self.assertEqual(user_email_call[1]["message"], message)
#         self.assertEqual(user_email_call[1]["from_email"], user_email)
#         self.assertEqual(user_email_call[1]["recipient_list"], [user_email])

# test_tasks.py
from unittest import mock
from django.test import TestCase, override_settings
from boosts.tasks import send_inspirational_to_beastie


@override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPAGATES=True)
class SendInspirationalToBeastieTest(TestCase):
    @mock.patch("boosts.tasks.send_mail")
    def test_send_inspirational_to_beastie(self, mock_send_mail):
        # Arrange
        user_username = "user123"
        user_email = "user@example.com"
        user_beastie_email = "beastie@example.com"
        user_beastie_username = "beastie123"
        message = "Keep pushing forward!"

        # Act
        send_inspirational_to_beastie(
            user_username,
            user_email,
            user_beastie_email,
            user_beastie_username,
            message,
        )

        # Assert
        self.assertEqual(mock_send_mail.call_count, 2)
        first_call_args, first_call_kwargs = mock_send_mail.call_args_list[0]
        second_call_args, second_call_kwargs = mock_send_mail.call_args_list[1]

        # Check first email (to beastie)
        self.assertEqual(
            first_call_args[0],
            f"Inspirational Quote from your Beastie: {user_username}",
        )
        self.assertEqual(first_call_args[1], message)
        self.assertEqual(first_call_args[2], user_email)
        self.assertEqual(first_call_args[3], [user_beastie_email])

        # Check second email (to user)
        self.assertEqual(
            second_call_args[0],
            f"You Sent an Inspirational Quote to your Beastie: {user_beastie_username}",
        )
        self.assertEqual(second_call_args[1], message)
        self.assertEqual(second_call_args[2], user_email)
        self.assertEqual(second_call_args[3], [user_email])
