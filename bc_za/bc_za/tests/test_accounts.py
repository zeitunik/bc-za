"""Test user account functionality."""
from django.contrib.auth import models as auth_models

from . import base


class LoginFormTests(base.SeleniumTestBase):
    """Test suite for user account functionality."""

    def setUp(self):
        """Prepare a user to work with etc."""
        super().setUp()
        self.credentials = {"username": "anders", "password": "ls8kjdf91a3sdf24"}
        self.user = auth_models.User.objects.create_user(
            self.credentials["username"], "anders@antonsen.dk", self.credentials["password"]
        )

    def test_login(self):
        """Test logging in a user."""
        self.get_literal_url("/accounts/login")
        self.fill({"#id_username": self.credentials["username"], "#id_password": self.credentials["password"]})
        self.submit("input[value='login']")
        session = self.get_session_data()
        self.assertEqual(session["_auth_user_id"], str(self.user.pk))

    def test_password_change(self):
        """
        Test changing the password.

        - Log in to change the password
        - Change the password
        - Log out
        - Log in with the new password
        """
        self.get_literal_url("/accounts/password_change")
        self.fill({"#id_username": self.credentials["username"], "#id_password": self.credentials["password"]})
        self.submit("input[value='login']")

        new_password = "s87234iuh§ao8s7dho34278"
        self.fill(
            {
                "#id_old_password": self.credentials["password"],
                "#id_new_password1": new_password,
                "#id_new_password2": new_password,
            }
        )
        self.submit("input[value='Change my password']")

        self.get_literal_url("/accounts/logout")

        self.get_literal_url("/accounts/login")
        self.fill({"#id_username": self.credentials["username"], "#id_password": new_password})
        self.submit("input[value='login']")
        session = self.get_session_data()
        self.assertEqual(session["_auth_user_id"], str(self.user.pk))
