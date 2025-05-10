# Comment testing for commit changes
# This script tracks workouts and provides a summary of the total time spent on each type of workout.
import datetime 


class Log:
    """
    A class to represent a workout log.
    
    Attributes:
        date (datetime.date): The date of the workout.
        workout_type (str): The type of workout.
        duration (int): The duration of the workout in minutes.
    """
    
    def __init__(self, date: datetime.date, workout_type: str, duration: int):
        self.date = date
        self.workout_type = workout_type
        self.duration = duration
        self.workout_log = []
        self.workout_summary = {}
        
    def add_workout(self, date: datetime.date, workout_type: str, duration: int):
        """
        Add a workout to the log.
            
        Parameters:
            date (datetime.date): The date of the workout.
            workout_type (str): The type of workout.
            duration (int): The duration of the workout in minutes.
        """
        self.workout_log.append({
            'date': date,
            'workout_type': workout_type,
            'duration': duration
        })
        self.update_summary(workout_type, duration)

    def update_summary(self, workout_type: str, duration: int):
        """
        Update the summary of workouts.
            
        Parameters:
            workout_type (str): The type of workout.
            duration (int): The duration of the workout in minutes.
        """
        if workout_type in self.workout_summary:
            self.workout_summary[workout_type] += duration
        else:
            self.workout_summary[workout_type] = duration
    
    def get_summary(self):
        """
        Get the summary of workouts.
            
        Returns:
            dict: A dictionary containing the total time spent on each type of workout.
        """
        return self.workout_summary
    
        