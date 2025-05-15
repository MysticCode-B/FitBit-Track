def calculate_bmi(weight_lbs: float, height_ft: float, height_in: float):
    """
    Calculate BMI using the formula: (weight / (height in inches ^ 2)) * 703
    
    Parameters:
        weight_lbs (float): Weight in pounds
        height_ft (float): Height in feet
        height_in (float): Height in inches

    Returns:
        float: BMI value rounded to 2 decimal places

    Raises: 
        ValueError: If height is zero or negative
    """
    if height_ft < 0 or height_in < 0:
        raise ValueError("Height cannot be negative.")
    
    total_height_in = (height_ft * 12) + height_in
    if total_height_in <= 0:
        raise ValueError("Height must be greater than zero.")
    
    bmi = (weight_lbs / (total_height_in ** 2)) * 703
    return round(bmi, 2)


def run_bmi_calculator(bmi: float):
    """
    Determine the BMI category based on the BMI range value.

    Parameters:
        bmi (float): BMI value

    Returns:
        str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"
