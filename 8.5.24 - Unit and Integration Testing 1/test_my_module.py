import unittest
from my_module import add  # Assume your function is in 'your_module.py'


class TestAddFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
