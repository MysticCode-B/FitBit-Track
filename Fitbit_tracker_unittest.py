import unittest
from unittest.mock import patch, mock_open
import json
import FitBit_Track as tracker  # Make sure your file is renamed accordingly

class TestFitnessTracker(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{}')
    @patch("os.path.exists", return_value=True)
    def test_load_data_existing_file(self, mock_exists, mock_file):
        data = tracker.load_data()
        self.assertEqual(data, {})

    @patch("builtins.open", new_callable=mock_open)
    def test_save_data(self, mock_file):
        data = {"test": "value"}
        tracker.save_data(data)
        mock_file.assert_called_with(tracker.DATA_FILE, 'w')
        handle = mock_file()
        handle.write.assert_called()

    @patch("builtins.input", side_effect=["shiv", "25", "5", "4", "130"])
    @patch("FitBit_Track.save_data")
    def test_create_profile(self, mock_save, mock_input):
        data = {}
        tracker.create_profile(data)
        self.assertIn("shiv", data["profiles"])
        self.assertEqual(data["profiles"]["shiv"]["age"], 25)
        mock_save.assert_called_once()

    @patch("builtins.input", side_effect=["shiv"])
    def test_calculate_bmi_option_profile_not_found(self, mock_input):
        data = {"profiles": {}}
        tracker.calculate_bmi_option(data)  # Should print "Profile not found."

    @patch("builtins.input", side_effect=["shiv"])
    def test_log_workout_no_profile(self, mock_input):
        data = {"profiles": {}}
        tracker.log_workout(data)  # Should print "Profile not found."

    @patch("builtins.input", side_effect=[
        "shiv",             # select profile
        "2023-05-01",       # date
        "Running",          # workout type
        "30"                # duration
    ])
    @patch("FitBit_Track.save_data")
    def test_log_workout_valid(self, mock_save, mock_input):
        from workout_tracker import Log
        data = {"profiles": {"shiv": {"workouts": []}}}
        tracker.log_workout(data)
        self.assertEqual(len(data["profiles"]["shiv"]["workouts"]), 1)
        self.assertEqual(data["profiles"]["shiv"]["workouts"][0]["workout_type"], "Running")
        mock_save.assert_called_once()

    @patch("builtins.input", side_effect=["shiv"])
    def test_file_summary_report_profile_not_found(self, mock_input):
        data = {"profiles": {}}
        tracker.file_summary_report(data)  # Should print "Profile not found."

if __name__ == '__main__':
    unittest.main()
