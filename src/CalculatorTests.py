import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_results(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subract(2, 2), 0)
        self.assertEqual(calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
