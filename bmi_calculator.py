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