import unittest
from src.bmi_calculator import BMICalculator

class TestBMICalculator(unittest.TestCase):

    def setUp(self):
        self.bmi_calculator = BMICalculator()

    def test_calculate_bmi(self):
        self.assertAlmostEqual(self.bmi_calculator.calculate_bmi(70, 1.75), 22.86, places=2)
        self.assertAlmostEqual(self.bmi_calculator.calculate_bmi(50, 1.60), 19.53, places=2)
        self.assertAlmostEqual(self.bmi_calculator.calculate_bmi(90, 1.80), 27.78, places=2)

    def test_get_bmi_category(self):
        self.assertEqual(self.bmi_calculator.get_bmi_category(22.86), 'Normal weight')
        self.assertEqual(self.bmi_calculator.get_bmi_category(19.53), 'Normal weight')
        self.assertEqual(self.bmi_calculator.get_bmi_category(27.78), 'Overweight')
        self.assertEqual(self.bmi_calculator.get_bmi_category(30), 'Obesity')

if __name__ == '__main__':
    unittest.main()