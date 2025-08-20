import unittest

class TestNone(unittest.TestCase):
    def setUp(self):
        self.value = None
        self.value_2 = 1

    def test_success(self):
        self.assertIsNone(self.value, "self.value is not None")

    def test_failure(self):
        self.assertIsNone(self.value_2, "self.value_2 is not None")

if __name__ == "__main__":
    unittest.main()