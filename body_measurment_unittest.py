import unittest
import datetime
from body_measurement import BodyMeasurementTracker

class TestBodyMeasurementTracker(unittest.TestCase):

    def setUp(self):
        """Initialize the tracker before each test."""
        self.tracker = BodyMeasurementTracker()
        self.test_date = datetime.date(2023, 10, 1)

    def test_log_measurement(self):
        """Test logging a new measurement."""
        self.tracker.log_measurement(self.test_date, 12.0, 32.0, 20.0)
        self.assertIn(self.test_date, self.tracker.measurements)
        self.assertEqual(self.tracker.measurements[self.test_date]["Arm Width"], 12.0)
        self.assertEqual(self.tracker.measurements[self.test_date]["Waist Width"], 32.0)
        self.assertEqual(self.tracker.measurements[self.test_date]["Leg Width"], 20.0)

    def test_update_measurement_success(self):
        """Test updating a measurement field successfully."""
        self.tracker.log_measurement(self.test_date, 12.0, 32.0, 20.0)
        self.tracker.update_measurement(self.test_date, **{"Arm Width": 13.5})
        self.assertEqual(self.tracker.measurements[self.test_date]["Arm Width"], 13.5)


    def test_update_measurement_invalid_date(self):
        """Test error raised when updating a date with no measurements."""
        with self.assertRaises(ValueError):
            self.tracker.update_measurement(datetime.date(2023, 10, 2), **{"Arm Width": 13.5})


    def test_update_measurement_invalid_field(self):
        """Test error raised when updating a non-existent field."""
        self.tracker.log_measurement(self.test_date, 12.0, 32.0, 20.0)
        with self.assertRaises(KeyError):
            self.tracker.update_measurement(self.test_date, Chest=40.0)

    def test_display_measurements_empty(self):
        """Test that display_measurements works with no data."""
        # This just ensures it doesn't crash; actual display is visual
        self.tracker.display_measurements()

    def test_display_measurements_with_data(self):
        """Test display_measurements with one entry."""
        self.tracker.log_measurement(self.test_date, 11.0, 30.0, 18.0)
        self.tracker.display_measurements()  # Visual verification; this won't raise an error

if __name__ == "__main__":
    unittest.main()
