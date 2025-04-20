import unittest
from workout_tracker import Log
import datetime

# filepath: /home/branc/Documents/UMD_Course/INST326_Final_Project/test_workout_tracker.py


class TestLog(unittest.TestCase):
    def setUp(self):
        """Set up a Log instance for testing."""
        self.log = Log(date=datetime.date(2023, 10, 1), workout_type="Running", duration=30)

    def test_add_workout(self):
        """Test the add_workout method."""
        # Add a workout
        self.log.add_workout(date=datetime.date(2023, 10, 2), workout_type="Cycling", duration=45)
        
        # Check if the workout was added correctly
        self.assertEqual(len(self.log.workout_log), 1)
        self.assertEqual(self.log.workout_log[0]['date'], datetime.date(2023, 10, 2))
        self.assertEqual(self.log.workout_log[0]['workout_type'], "Cycling")
        self.assertEqual(self.log.workout_log[0]['duration'], 45)

if __name__ == "__main__":
    unittest.main()