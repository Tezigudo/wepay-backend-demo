import unittest
from models import User, Bill


class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.user0 = User('user0')

    def test_user_id(self):
        """check whether user id is correct"""
        self.assertEqual(self.user0.user_id, 1)
        user1 = User('user1')
        self.assertEqual(user1.user_id, 2)
