import unittest
from csv import *
from calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_instantiate_object(self):
        self.assertIsInstance(self.calc, Calculator)

    def run_test(self, filepath, method):
        self.method = method
        with open(filepath) as data_file:
            test_data = DictReader(data_file)
            for row in test_data:
                val1 = row["Value 1"]
                try:
                    val2 = row["Value 2"]
                except:
                    pass
                result = row["Result"]
                if self.method == 'add':
                    self.assertEqual(self.calc.add(int(val1), int(val2)), int(result))
                if self.method == 'sub':
                    self.assertEqual(self.calc.sub(int(val1), int(val2)), int(result))
                if self.method == 'mul':
                    self.assertEqual(self.calc.mul(int(val1), int(val2)), int(result))
                if self.method == 'div':
                    self.assertAlmostEqual(
                        self.calc.div(int(val1), int(val2)), float(result))
                if self.method == 'sqr':
                    self.assertAlmostEqual(self.calc.sqr(int(val1)), int(result))
                if self.method == 'sqroot':
                    self.assertAlmostEqual(self.calc.sqroot(int(val1)), float(result))

    def test_addition(self):
        self.run_test('src/test-data/Unit Test Addition.csv', 'add')

    def test_subtraction(self):
        self.run_test('src/test-data/Unit Test Subtraction.csv', 'sub')

    def test_multiplication(self):
        self.run_test('src/test-data/Unit Test Multiplication.csv', 'mul')

    def test_division(self):
        self.run_test('src/test-data/Unit Test Division.csv', 'div')

    def test_square(self):
        self.run_test('src/test-data/Unit Test Square.csv', 'sqr')

    def test_square_root(self):
        self.run_test('src/test-data/Unit Test Square Root.csv', 'sqroot')


if __name__ == '__main__':
    unittest.main()
