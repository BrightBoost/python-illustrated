def convert_temperature(temp_value, mode="CtoF"):
    """
    Convert temperatures between Celsius and Fahrenheit.
    
    Parameters:
    temp_value: The temperature to be converted.
    mode: The conversion mode, either "CtoF" for Celsius to Fahrenheit or "FtoC" for Fahrenheit to Celsius. Defaults to "CtoF".
    
    Returns the converted temperature.
    """
    if mode == "CtoF":  # Celsius to Fahrenheit
        return (temp_value * 9/5) + 32
    elif mode == "FtoC":  # Fahrenheit to Celsius
        return (temp_value - 32) * 5/9

# Test cases
print(convert_temperature(99))  # Default: 99°C → Fahrenheit
print(convert_temperature(77, "FtoC"))  # 77°F → Celsius
print(convert_temperature(0))  # 0°C → Fahrenheit
print(convert_temperature(100, "CtoF"))  # 100°C → Fahrenheit


