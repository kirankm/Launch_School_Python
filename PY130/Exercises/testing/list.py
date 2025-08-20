import unittest

class TestList(unittest.TestCase):
    def setUp(self):
        self.lst = ['xyz', 'abc']

    def test_success(self):
        self.assertIn('xyz', self.lst, f'value not in {self.lst}')

    def test_failure(self):
        self.assertIn('XYZ', self.lst, f'value not in {self.lst}')

if __name__ == "__main__":
    unittest.main()


