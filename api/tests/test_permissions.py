from django.test import TestCase
from unittest.mock import Mock
from api.permissions import IsRegistrationAccepted, IsStaff


class IsRegistrationAcceptedTest(TestCase):
    def setUp(self):
        self.permission = IsRegistrationAccepted()
        self.request = Mock()

    def test_permission_granted(self):
        self.request.user = Mock(registration_accepted=True)
        self.assertTrue(self.permission.has_permission(self.request, None))

    def test_permission_denied(self):
        self.request.user = Mock(registration_accepted=False)
        self.assertFalse(self.permission.has_permission(self.request, None))


class IsStaffTest(TestCase):
    def setUp(self):
        self.permission = IsStaff()
        self.request = Mock()

    def test_staff_permission_granted(self):
        self.request.user = Mock(is_staff=True)
        self.assertTrue(self.permission.has_permission(self.request, None))

    def test_staff_permission_denied(self):
        self.request.user = Mock(is_staff=False)
        self.assertFalse(self.permission.has_permission(self.request, None))
