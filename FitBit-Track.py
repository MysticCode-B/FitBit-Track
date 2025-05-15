import json
import os
from workout_tracker import Log
from bmi_calculator import run_bmi_calculator, calculate_bmi
from body_measurement import BodyMeasurementTracker

# File path for storing user data
DATA_FILE = "fitness_data.json"

# Load user data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent = 4)

# Main Menu
def main_menu():
    print("\n--- Fitness Tracker ---")
    print("1. Create Profile")
    print("2. Log Workout")
    print("3. Calculate BMI")
    print("4. Track Body Measurements")
    print("5. View Summary Report")
    print("6. Exit")

    choice = input("Select an option: ")
    return choice

# Create user profile
def create_profile(data):
    if 'profiles' not in data:
        data['profiles'] = {}

    name = input("Enter your name: ")
    if name in data['profiles']:
        print("A profile with this name already exists. Please choose a different name.")
        return

    age = int(input("Enter your age: "))
    try:
        height_ft = float(input("Enter your height in feets: "))
        height_in = float(input("Enter your height in inches: "))
        weight = float(input("Enter your weight in lbs: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")
        return

    data['profiles'][name] = {
        'age': age,
        'height_ft': height_ft,
        'height_in': height_in,
        'weight': weight,
        'measurements': {},
        'workouts': []
    }
    save_data(data)
    print("Profile created successfully!\n")

def log_workout(data):
    if 'profiles' not in data:
        print("Please create a profile first.")
        return
    
    name = input("Enter your name: ")
    if name not in data['profiles']:
        print("Profile not found.")
        return

    date = input("Enter the date of the workout (YYYY-MM-DD): ")
    workout_type = input("Enter the type of workout: ")
    duration = int(input("Enter the duration of the workout in minutes: "))

    log = Log(date, workout_type, duration)
    data['profiles']['workouts'].append(log.__dict__)
    save_data(data)
    print("Workout logged successfully!\n")

# This will calculate the BMI from imports when the user selects the option
def calculate_bmi(data):
    if 'profiles' not in data:
        print("Please create a profile first.")
        return

    name = input("Enter your name: ")
    if name not in data['profiles']:
        print("Profile not found. Please create a profile first.")
        return

    profile = data['profiles'][name]
    weight = profile['weight']
    height_ft = profile['height_ft']
    height_in = profile['height_in']


    # importing the function from bmi_calculator.py
    bmi = calculate_bmi(weight, height_ft)
    category = run_bmi_calculator(bmi)
    print(f"\nYour BMI is: {bmi}")
    print(f"You are in the '{category}' category.\n")

def body_measurments_tracker(data):
    if 'profiles' not in data:
        print("Please create a profile first.")
        return

    tracker = BodyMeasurementTracker()
    date = input("Enter the date of the measurement (YYYY-MM-DD): ")
    arm_width = float(input("Enter arm width in inches: "))
    waist_width = float(input("Enter waist width in inches: "))
    leg_width = float(input("Enter leg width in inches: "))

    tracker.log_measurement(date, arm_width, waist_width, leg_width)
    data['profiles']['measurements'][date] = tracker.measurements[date]
    save_data(data)
    print("Body measurements logged successfully!\n")

def file_summary_report(data):
    if 'profiles' not in data:
        print("Please create a profile first.")
        return

    print("\n--- Summary Report ---")
    print(f"Name: {data['profile']['name']}")
    print(f"Age: {data['profile']['age']}")
    print(f"Height: {data['profile']['height_ft']['height_in']}")
    print(f"Weight: {data['profile']['weight']} kg")
    
    if 'workouts' in data['profiles']:
        print("\nWorkouts:")
        for workout in data['profiles']['workouts']:
            print(f"  Date: {workout['date']}, Type: {workout['workout_type']}, Duration: {workout['duration']} minutes")

    if 'measurements' in data['profiles']:
        print("\nBody Measurements:")
        for date, measurements in data['profiles']['measurements'].items():
            print(f"  Date: {date}, Arm Width: {measurements['Arm Width']} inches, Waist Width: {measurements['Waist Width']} inches, Leg Width: {measurements['Leg Width']} inches")

    print("-" * 20)
    print("Summary report generated successfully!\n")

def main():
    data = load_data()

    while True:
        choice = main_menu()
        
        if choice == '1':
            create_profile(data)
        elif choice == '2':
            log_workout(data)
        elif choice == '3':
            calculate_bmi(data)
        elif choice == '4':
            body_measurments_tracker(data)
        elif choice == '5':
            file_summary_report(data)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
        print("\n")


if __name__ == "__main__":
    main()