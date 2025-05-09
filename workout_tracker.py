# Comment testing for commit changes
# This script tracks workouts and provides a summary of the total time spent on each type of workout.
import datetime 
import re
import os
import sys
import json

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
    
def main():
    # Create a Log object
    log = Log(datetime.date.today(), '', 0)
    
    # take user input for workouts
    workouts = []
    while True:
        date_input = input("Enter the date of the workout (YYYY-MM-DD) or 'done' to finish: ")
        if date_input.lower() == 'done':
            break
        try:
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
            continue
        
        workout_type = input("Enter the type of workout: ")
        duration_input = input("Enter the duration of the workout in minutes: ")
        
        try:
            duration = int(duration_input)
        except ValueError:
            print("Invalid duration. Please enter a number.")
            continue
        
        workouts.append((date, workout_type, duration))
    
    # Add workouts to the log
    for date, workout_type, duration in workouts:
        log.add_workout(date, workout_type, duration)
    
    # Get the summary of workouts
    summary = log.get_summary()
    
    # Print the summary
    print("Workout Summary:")
    for workout_type, total_duration in summary.items():
        print(f"{workout_type}: {total_duration} minutes")
    # Save the log to a file
    with open('workout_log.json', 'w') as f:
        json.dump(log.workout_log, f, default=str)
    
if __name__ == "__main__":
    main()
# This script tracks workouts and provides a summary of the total time spent on each type of workout.
        