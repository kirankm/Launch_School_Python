import unittest

class TestBoolean(unittest.TestCase):
    def setUp(self):
        self.value = 4

    def test_boolean(self):
        self.assertTrue(self.value %2 != 0)

if __name__ == "__main__":
    unittest.main()