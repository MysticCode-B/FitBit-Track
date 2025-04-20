import datetime

class BodyMeasurementTracker:
    """
    A simple tracker for logging body measurements.
    
    Attributes:
        measurements (dict): Stores the measurements with timestamps.
    """

    def __init__(self):
        self.measurements = {}
    
    def log_measurement(self, date: datetime.date, arm_width: float, waist_width: float, leg_width: float):
        """
        Log a new set of body measurements.

        Parameters:
            date (datetime.date): The date of the measurement.
            arm_width (float): Arm width in inches.
            waist_width (float): Waist width in inches.
            leg_width (float): Leg width in inches.
        """
        self.measurements[date] = {
            "Arm Width": arm_width,
            "Waist Width": waist_width,
            "Leg Width": leg_width
        }
    
    def update_measurement(self, date: datetime.date, **kwargs):
        """
        Update specific measurements for a given date.

        Parameters:
            date (datetime.date): The date of the measurement to update.
            kwargs: Measurement fields to update (e.g., Arm Width, Waist Width).
        """
        if date not in self.measurements:
            raise ValueError("No measurements logged for this date.")
        
        for key, value in kwargs.items():
            if key in self.measurements[date]:
                self.measurements[date][key] = value
            else:
                raise KeyError(f"Invalid measurement field: {key}")
    
    def display_measurements(self):
        """Display all logged measurements."""
        if not self.measurements:
            print("No measurements logged yet.")
            return
        
        for date, data in sorted(self.measurements.items()):
            print(f"Date: {date}")
            for key, value in data.items():
                print(f"  {key}: {value} inches")
            print("-" * 20)

# Example Usage:
tracker = BodyMeasurementTracker()

# Log initial measurements
tracker.log_measurement(datetime.date(2025, 4, 20), arm_width=12.5, waist_width=30.0, leg_width=22.0)

# Update a measurement
tracker.update_measurement(datetime.date(2025, 4, 20), Arm_Width=13.0)

# Display all measurements
tracker.display_measurements()
