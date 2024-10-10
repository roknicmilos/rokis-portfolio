from django.contrib.admin import AdminSite
from django.test import TestCase

from apps.user.admin import UserAdmin
from apps.user.models import User
from apps.user.tests.factories import UserFactory


class UserAdminTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.site = AdminSite()
        self.admin = UserAdmin(User, self.site)
        self.request = self.client.get("/").wsgi_request
        self.staff_user = UserFactory.create_staff_user()
        self.superuser = UserFactory.create_superuser()

    def test_get_queryset(self):
        """
        When the current user is not a superuser, the queryset
        should return only the users that belong to the user.
        When the current user is a superuser, the queryset should
        return all the users.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        queryset = self.admin.get_queryset(self.request)
        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first(), self.staff_user)

        # Test when the current user is a superuser
        self.request.user = self.superuser
        queryset = self.admin.get_queryset(self.request)
        self.assertEqual(queryset.count(), 2)
        self.assertEqual(set(queryset), {self.staff_user, self.superuser})

    def test_list_display(self):
        """
        When the current user is not a superuser, the list_display
        should be the same as the one defined in the UserAdmin class.
        When the current user is a superuser, the list_display
        should be the same as the one defined in superuser_list_display.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        actual_list_display = self.admin.get_list_display(self.request)
        self.assertEqual(actual_list_display, self.admin.list_display)

        # Test when the current user is a superuser
        self.request.user = self.superuser
        actual_list_display = self.admin.get_list_display(self.request)
        self.assertEqual(actual_list_display, self.admin.superuser_list_display)

    def test_get_fieldsets(self):
        """
        When the current user is not a superuser, the fieldsets
        should be the same as the ones defined in the UserAdmin class.
        When the current user is a superuser, the fieldsets
        should be the same as the ones defined in superuser_fieldsets.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        actual_fieldsets = self.admin.get_fieldsets(self.request)
        self.assertEqual(actual_fieldsets, self.admin.fieldsets)

        # Test when the current user is a superuser
        self.request.user = self.superuser
        actual_fieldsets = self.admin.get_fieldsets(self.request)
        self.assertEqual(actual_fieldsets, self.admin.superuser_fieldsets)

    def test_get_search_fields(self):
        """
        When the current user is not a superuser, the search_fields
        should be an empty tuple.
        When the current user is a superuser, the search_fields
        should be the same as the one defined in the UserAdmin class.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        actual_search_fields = self.admin.get_search_fields(self.request)
        self.assertEqual(actual_search_fields, ())

        # Test when the current user is a superuser
        self.request.user = self.superuser
        actual_search_fields = self.admin.get_search_fields(self.request)
        self.assertEqual(actual_search_fields, self.admin.search_fields)

    def test_list_filter(self):
        """
        When the current user is not a superuser, the list_filter
        should be empty.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        actual_list_filter = self.admin.get_list_filter(self.request)
        self.assertEqual(actual_list_filter, ())

        # Test when the current user is a superuser
        self.request.user = self.superuser
        actual_list_filter = self.admin.get_list_filter(self.request)
        self.assertEqual(actual_list_filter, self.admin.list_filter)

    def test_get_actions(self):
        """
        When the current user is not a superuser, the actions
        should be empty.
        """
        # Test when the current user is not a superuser
        self.request.user = self.staff_user
        actual_list_filter = self.admin.get_actions(self.request)
        self.assertEqual(actual_list_filter, ())

        # Test when the current user is a superuser
        self.request.user = self.superuser
        actual_list_filter = self.admin.get_actions(self.request)
        self.assertEqual(len(actual_list_filter), 1)
