import unittest

def square(n): return n * n
def cube(n): return n ** 3
def add(a, b): return a + b

class TestMathOperations(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)

    def test_cube(self):
        self.assertEqual(cube(3), 27)

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

if __name__ == '__main__':
    unittest.main()

