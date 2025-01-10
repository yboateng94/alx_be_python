# temp_conversion_tool.py

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius using global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit using global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def get_temperature_input():
    """Get user input for temperature value and unit."""
    while True:
        try:
            temp_input = input("Enter a temperature (e.g., 32F, 0C): ").strip()
            if temp_input[-1].upper() == 'F':  # Fahrenheit input
                temp_value = float(temp_input[:-1])
                return temp_value, 'F'
            elif temp_input[-1].upper() == 'C':  # Celsius input
                temp_value = float(temp_input[:-1])
                return temp_value, 'C'
            else:
                print("Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def main():
    # Prompt the user to enter temperature
    temp_value, unit = get_temperature_input()

    # Perform conversion and display result
    if unit.upper() == 'F':
        converted_temp = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is equal to {converted_temp:.2f}°C.")
    elif unit.upper() == 'C':
        converted_temp = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is equal to {converted_temp:.2f}°F.")

if __name__ == "__main__":
    main()
