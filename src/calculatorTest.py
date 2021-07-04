import unittest
from calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_instantiate_calc(self):
        self.assertIsInstance(self.calc, Calculator)


if __name__ == '__main__':
    unittest.main()
