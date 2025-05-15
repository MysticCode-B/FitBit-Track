import unittest
from bmi_calculator import calculate_bmi, run_bmi_calculator

class TestBMICalculator(unittest.TestCase):

    def test_calculate_bmi_valid_input(self):
        """Test BMI calculation with valid height and weight."""
        bmi = calculate_bmi(weight_lbs=150, height_ft=5, height_in=6)
        self.assertAlmostEqual(bmi, 24.21, places=2)

    def test_calculate_bmi_zero_height(self):
        """Test BMI calculation raises ValueError for zero height."""
        with self.assertRaises(ValueError):
            calculate_bmi(weight_lbs=150, height_ft=0, height_in=0)

    def test_calculate_bmi_negative_height(self):
        """Test BMI calculation raises ValueError for negative height."""
        with self.assertRaises(ValueError):
            calculate_bmi(weight_lbs=150, height_ft=-5, height_in=6)

    def test_run_bmi_calculator_underweight(self):
        """Test BMI category for underweight."""
        self.assertEqual(run_bmi_calculator(17.0), "Underweight")

    def test_run_bmi_calculator_normal(self):
        """Test BMI category for normal weight."""
        self.assertEqual(run_bmi_calculator(22.5), "Normal weight")

    def test_run_bmi_calculator_overweight(self):
        """Test BMI category for overweight."""
        self.assertEqual(run_bmi_calculator(27.3), "Overweight")

    def test_run_bmi_calculator_obese(self):
        """Test BMI category for obese."""
        self.assertEqual(run_bmi_calculator(30.5), "Obese")

if __name__ == "__main__":
    unittest.main()
