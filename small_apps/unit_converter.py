# Unit Converter
# Converts Unit to unified base unit, and then to the desired unit

# Temperature

to_celsius = {
    "from_celsius": 1,
    "from_kelvin": -273.15,
    "from_fahrenheit": -32 * 5/9
}

unit_temp = input("Select what to convert from >> ")
temp = float(input(f"How many {unit_temp} to Celsius?"))

if unit_temp == "Kelvin":
    print(f"{temp} Kelvin = {temp, to_celsius["from_kelvin"]} Celsius")





def get_celsius(temp, base_unit):
    temp = float(temp)
    if base_unit == "Celsius":
        return temp
    elif base_unit == "Fahrenheit":
        return (temp - 32) * 5/9
    elif base_unit == "Kelvin":
        return temp - 273.15
    else: raise ValueError(f"Unknown unit: {base_unit}")

def get_temperature(temp, base_unit, end_unit):
    celsius = float(get_celsius(temp, base_unit))
    if end_unit == "Celsius":
        return celsius
    elif end_unit == "Fahrenheit":
        return (celsius * 9 / 5) + 32
    elif end_unit == "Kelvin":
        return celsius + 273.15
    else: raise ValueError(f"Unknown unit: {end_unit}")
