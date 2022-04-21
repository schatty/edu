from django.test import TestCase
from django.test import Client


class UserProfileLoginTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            "username": "TestUser",
            "email": "testuser@everel.local",
            "password1": "TestUserPassword",
            "password2": "TestUserPassword"
        }

        Client().post(
            "/eauth/register/",
            data=cls.user_data
        )

    def test_signin(self):
        signin_response = self.client.post(
            "/eauth/login/",
            data=self.user_data
        )
        self.assertEqual(200, signin_response.status_code)

        signout_response = self.client.post(
            "/eauth/logout",
        )
        self.assertIn(signout_response.status_code, (301, 302))

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # print("Sign in / out: OK.")