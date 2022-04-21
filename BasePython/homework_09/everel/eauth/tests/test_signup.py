from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UserProfileRegisterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            "username": "TestUser",
            "email": "testuser@everel.local",
            "password1": "TestUserPassword",
            "password2": "TestUserPassword"
        }
        cls.user_broken_data = {
            "username": "TestUser",
            "email": "testuser@everel.local",
            "password1": "TestUserPassword",
            "password2": "TestUserP@ssword"
        }

    def test_success_register(self):
        response = self.client.post(
            "/eauth/register/",
            data=self.user_data
        )
        self.assertEqual(302, response.status_code)

        new_user = get_user_model().objects.get(
            username=self.user_data["username"]
        )

        self.assertEqual(self.user_data["email"],
                         new_user.email)

    def test_fail_register(self):
        response = self.client.post(
            reverse("eauth:register"),
            data=self.user_broken_data
        )
        self.assertEqual(200, response.status_code)
        self.assertFormError(
            response,
            'form',
            'password2',
            "The two password fields didn’t match."
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # print("Sign up: OK.")