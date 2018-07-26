import unittest
import firebase_admin
from src.service.UserService import UserService
from src.client.FirebaseClient import FirebaseClient
from src.model.User import User

class UserServiceTest(unittest.TestCase):

    def setUp(self):
        self.firebaseClient = FirebaseClient()
        self.test_user_service = UserService(self.firebaseClient)

        self.is_setup = False
        self.TEST_FIRST_NAME = "test_first_name"
        self.TEST_LAST_NAME = "test_last_name"
        self.TEST_ID = "test_id"
        self.CHANGED_NAME = "test_changed_name"

    def tearDown(self):
        firebase_admin.delete_app(firebase_admin.get_app())

    def test_initialize_user(self):
        """
        Test if user can be properly initialized
        """
        self.test_user_service.initialize_user(self.TEST_FIRST_NAME, self.TEST_LAST_NAME)

        self.assertEquals(self.test_user_service.target_user.first_name, self.TEST_FIRST_NAME)
        self.assertEquals(self.test_user_service.target_user.last_name, self.TEST_LAST_NAME)
        self.assertIsNotNone(self.test_user_service.target_user.id)


    def test_edit_user_info(self):
        """
        Test to see that user info can be edited correctly
        """

        target_field_name = "first_name"

        test_user = User(self.TEST_ID, self.TEST_FIRST_NAME, self.TEST_LAST_NAME)
        self.test_user_service.target_user = test_user
        self.test_user_service.edit_user_info(self.TEST_ID, target_field_name, self.CHANGED_NAME)

        self.assertEquals(self.test_user_service.target_user.first_name, self.CHANGED_NAME)

