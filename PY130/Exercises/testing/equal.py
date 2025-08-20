import unittest

class TestEquality(unittest.TestCase):
    def setUp(self):
        self.value = "XyZ"
        self.value_2 = 'yz'

    def test_success(self):
        self.assertEqual("xyz", self.value.lower(), "lower case value is not xyz")

    def test_fail(self):
        self.assertEqual("xyz", self.value_2.lower(), "lower case value is not xyz")

if __name__ == "__main__":
    unittest.main()