import json
import os
from workout_tracker import Log
from bmi_calculator import run_bmi_calculator, calculate_bmi as bmi_calculator
from body_measurement import BodyMeasurementTracker


DATA_FILE = "fitness_data.json"

#Load user data from file 
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user data to file 
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

#Main Menu
def main_menu():
    print("\n--- Fitness Tracker ---")
    print("1. Create Profile")
    print("2. Log Workout")
    print("3. Calculate BMI")
    print("4. Track Body Measurements")
    print("5. View Summary Report")
    print("6. Exit")
    return input("Select an option: ")

# Create user Profile 
def create_profile(data):
    if 'profiles' not in data:
        data['profiles'] = {}

    name = input("Enter your name: ")
    if name in data['profiles']:
        print("A profile with this name already exists. Please choose a different name.")
        return

    try:
        age = int(input("Enter your age: "))
        height_ft = float(input("Enter your height in feet: "))
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
    if 'profiles' not in data or not data['profiles']:
        print("Please create a profile first.")
        return

    # Ask the user to select a profile 
    print("Available profiles:")
    for name in data['profiles']:
        print(f"- {name}")
    name = input("Enter the name of the profile to log the workout: ")

    if name not in data['profiles']:
        print("Profile not found.")
        return

   
    #log the workout for the select profile 
    date = input("Enter the date of the workout (YYYY-MM-DD): ")
    workout_type = input("Enter the type of workout: ")
    try:
        duration = int(input("Enter the duration of the workout in minutes: "))
    except ValueError:
        print("Invalid input for duration.")
        return

    log = Log(date, workout_type, duration)
    data['profiles'][name]['workouts'].append(log.__dict__) #Update the correct profile's workout
    save_data(data)
    print("Workout logged successfully!\n")
    
# This will calculate the BMI from imports when the user selects the option
def calculate_bmi_option(data):
    if 'profiles' not in data or not data['profiles']:
        print("Please create a profile first.")
        return

    name = input("Enter your name: ")
    if name not in data['profiles']:
        print("Profile not found.")
        return

    profile = data['profiles'][name]
    #importing the function from bmi_calculator.py
    bmi = bmi_calculator(profile['weight'], profile['height_ft'], profile['height_in']) 
    category = run_bmi_calculator(bmi)
    print(f"\nYour BMI is: {bmi}")
    print(f"You are in the '{category}' category.\n")

def body_measurements_tracker(data):
    if 'profiles' not in data or not data['profiles']:
        print("Please create a profile first.")
        return

    print("Available profiles:")
    for name in data['profiles']:
        print(f"- {name}")
    name = input("Enter the name to log body measurements: ")

    if name not in data['profiles']:
        print("Profile not found.")
        return

    tracker = BodyMeasurementTracker()
    try:
        date = input("Enter the date of the measurement (YYYY-MM-DD): ")
        arm_width = float(input("Enter arm width in inches: "))
        waist_width = float(input("Enter waist width in inches: "))
        leg_width = float(input("Enter leg width in inches: "))
    except ValueError:
        print("Invalid input for measurements.")
        return

    tracker.log_measurement(date, arm_width, waist_width, leg_width)
    data['profiles'][name]['measurements'][date] = tracker.measurements[date]
    save_data(data)
    print("Body measurements logged successfully!\n")

def file_summary_report(data):
    if 'profiles' not in data or not data['profiles']:
        print("Please create a profile first.")
        return

    print("Available profiles:")
    for name in data['profiles']:
        print(f"- {name}")
    name = input("Enter the name to view summary: ")

    if name not in data['profiles']:
        print("Profile not found.")
        return

    profile = data['profiles'][name]
    print("\n--- Summary Report ---")
    print(f"Name: {name}")
    print(f"Age: {profile['age']}")
    print(f"Height: {profile['height_ft']} ft {profile['height_in']} in")
    print(f"Weight: {profile['weight']} lbs")

    if profile['workouts']:
        print("\nWorkouts:")
        for workout in profile['workouts']:
            print(f"  Date: {workout['date']}, Type: {workout['workout_type']}, Duration: {workout['duration']} minutes")

    if profile['measurements']:
        print("\nBody Measurements:")
        for date, measurements in profile['measurements'].items():
            print(f"  Date: {date}, Arm Width: {measurements['Arm Width']} in, Waist Width: {measurements['Waist Width']} in, Leg Width: {measurements['Leg Width']} in")

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
            calculate_bmi_option(data)
        elif choice == '4':
            body_measurements_tracker(data)
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
