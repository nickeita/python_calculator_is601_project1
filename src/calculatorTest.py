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

    def test_multiplication(self):
        with open('src/Unit Test Multiplication.csv') as multiplication_file:
            multiplication_data = DictReader(multiplication_file)
            for row in multiplication_data:
                a = row["Value 1"]
                b = row["Value 2"]
                c = row["Result"]
                self.assertEqual(self.calc.mul(int(a), int(b)), int(c))

    def test_division(self):
        with open('src/Unit Test Division.csv') as division_file:
            division_data = DictReader(division_file)
            for row in division_data:
                a = row["Value 1"]
                b = row["Value 2"]
                c = row["Result"]
                self.assertAlmostEqual(self.calc.div(int(a), int(b)), float(c))

    def test_square(self):
        with open('src/Unit Test Square.csv') as square_file:
            square_data = DictReader(square_file)
            for row in square_data:
                a = row["Value 1"]
                b = row["Result"]
                self.assertAlmostEqual(self.calc.sqr(int(a)), int(b))


if __name__ == '__main__':
    unittest.main()
