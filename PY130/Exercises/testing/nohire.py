import unittest

class TestException(unittest.TestCase):
    def setUp(self):
        self.employee = None

    def test_exception(self):
        with self.assertRaises(NoExperienceError):
            self.employee.hire()
            self.assertIs()

if __name__ == "__main__":
    unittest.main()