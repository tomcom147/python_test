import unittest
import A017

class TestA017(unittest.TestCase):
    def test_add(self):
        self.assertEqual(A017.makeField, 3)

if __name__ == "__main__":
    unittest.main()