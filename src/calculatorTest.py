import unittest
from csv import DictReader
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    calc_data = {}

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_instantiate_objects(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition(self):
        with open('src/test-data/Unit Test Addition.csv') as csv_file:
            calc_data = DictReader(csv_file)
        for row in self.calc_data:
            a = row["Value 1"]
            b = row["Value 2"]
            c = row["Result"]
            self.assertEqual(self.calc.add(int(a), int(b)), int(c))


if __name__ == '__main__':
    unittest.main()
