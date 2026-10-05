def convert_temperature(value, unit="Fahrenheit"):
    if unit == "Fahrenheit":
        return value * 9/5 + 32
    elif unit == "Kelvin":
        return value + 50
    else:
        return "Invalid unit"

celsius = 30
fahrenheit = convert_temperature(celsius)
kelvin = convert_temperature(celsius, "Kelvin")
print("Celsius to Fahrenheit", fahrenheit)
print("Celsius to Kelvin",kelvin)
