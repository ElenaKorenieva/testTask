import unittest
from math import isclose
from main import Square, Rectangle, Circle, Triangle, create_shape

class TestShapes(unittest.TestCase):

    def test_square(self):
        s = Square(2)
        self.assertEqual(s.perimeter(), 8)
        self.assertEqual(s.area(), 4)

    def test_rectangle(self):
        r = Rectangle(4, 5, 1, 1)
        self.assertEqual(r.perimeter(), 14)
        self.assertEqual(r.area(), 12)

    def test_circle(self):
        c = Circle(3)
        self.assertTrue(isclose(c.perimeter(), 2 * 3.1416 * 3, rel_tol=1e-2))
        self.assertTrue(isclose(c.area(), 3.1416 * 9, rel_tol=1e-2))

    def test_triangle(self):
        t = Triangle(0, 0, 4, 0, 0, 3)
        self.assertTrue(isclose(t.perimeter(), 12.0, rel_tol=1e-2))
        self.assertTrue(isclose(t.area(), 6.0, rel_tol=1e-2))

    def test_create_shape_square(self):
        shape = create_shape("Square TopRight 1 1 Side 2")
        self.assertIsInstance(shape, Square)
        self.assertEqual(shape.area(), 4)

    def test_create_shape_invalid(self):
        with self.assertRaises(ValueError):
            create_shape("Hexagon Center 0 0 Side 2")

if __name__ == "__main__":
    unittest.main()
