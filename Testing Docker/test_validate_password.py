import unittest
from utils import validate_password

class PasswordValidationTest(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("PassValid1!"))
        self.assertTrue(validate_password("StrongPassword1@"))
        self.assertTrue(validate_password("Another$Valid2"))

    def test_invalid_password_length(self):
        self.assertFalse(validate_password("Short1!"))
        self.assertFalse(validate_password("NoSpecialChar1"))

    def test_invalid_password_no_uppercase(self):
        self.assertFalse(validate_password("invalidpassword1!"))

    def test_invalid_password_no_lowercase(self):
        self.assertFalse(validate_password("INVALIDPASSWORD1!"))

    def test_invalid_password_no_digit(self):
        self.assertFalse(validate_password("NoDigit!"))

    def test_invalid_password_no_special_char(self):
        self.assertFalse(validate_password("NoSpecialChar1"))

if __name__ == '__main__':
    unittest.main()