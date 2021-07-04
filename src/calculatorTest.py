import unittest
from csv import DictReader
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_instantiate_objects(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition(self):
        with open('src/Unit Test Addition.csv') as addition_file:
            addition_data = DictReader(addition_file)
            for row in addition_data:
                a = row["Value 1"]
                b = row["Value 2"]
                c = row["Result"]
                self.assertEqual(self.calc.add(int(a), int(b)), int(c))

    def test_subtraction(self):
        with open('src/Unit Test Subtraction.csv') as subtraction_file:
            subtraction_data = DictReader(subtraction_file)
            for row in subtraction_data:
                a = row["Value 1"]
                b = row["Value 2"]
                c = row["Result"]
                self.assertEqual(self.calc.sub(int(a), int(b)), int(c))


if __name__ == '__main__':
    unittest.main()
