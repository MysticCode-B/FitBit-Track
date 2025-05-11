def calculate_bmi(weight_lbs: float, height_ft: int, height_in: int):
    """
    Calculate BMI using the formula: (weight / (height in inches ^ 2)) * 703
    
    Parameters:
        weight_lbs (float): Weight in pounds
        height_ft (int): Height in feet
        height_in (int): Height in inches

    Returns:
        float: BMI value rounded to 2 decimal places

    Raises: 
        ValueError: If height is zero or negative
    """
    if height_ft < 0 or height_in < 0:
        raise ValueError("Height cannot be negative.")
    
    # it convert height to inches
    total_height_in = (height_ft * 12) + height_in
    
    if total_height_in <= 0:
        raise ValueError("Height must be greater than zero.")
    
    # It is a BMI calculation
    bmi = (weight_lbs / (total_height_in ** 2)) * 703
    return round(bmi, 2)

def bmi_category(bmi: float):
    """
    It determine the BMI category based on the BMI range value.
    Parameters:
        bmi (float): It is a BMI number
    Returns:
        str: A string shows and tells the BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
def run_bmi_calculator():
    """
    Run the BMI calculator by asking the user for weight and height,
    then showing their BMI and category.
    """
    try:
        weight = float(input("Enter your weight in pounds (lbs): "))
        feet = int(input("Enter your height (Feet): "))
        inches = int(input("Enter your height (Inches): "))
        bmi = calculate_bmi(weight, feet, inches)
        category = bmi_category(bmi)
        print(f"\nYour BMI is: {bmi}")
        print(f"You are in the '{category}' category.")
    
    except ValueError as e:
        print(f"Error: {e}")
# If this file is run directly, start the calculator
if __name__ == "__main__":
    run_bmi_calculator()
