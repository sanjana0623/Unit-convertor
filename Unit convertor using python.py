#!/usr/bin/env python
# coding: utf-8

# # Unit Converter

# In[3]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def display_menu():
    print("\nUnit Converter")
    print("Select a conversion type:")
    print("1. Temperature Converter (°C to °F / °F to °C)")
    print("2. Length Converter (Meters to Feet / Feet to Meters)")
    print("3. Weight Converter (Kilograms to Pounds / Pounds to Kilograms)")
    print("4. Quit")

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_temperature_conversion():
    print("\nTemperature Converter")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")
    conversion_type = get_user_input("Enter your choice: ")
    if conversion_type == '1':
        celsius = float(get_user_input("Enter the temperature in °C: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif conversion_type == '2':
        fahrenheit = float(get_user_input("Enter the temperature in °F: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def perform_length_conversion():
    print("\nLength Converter")
    print("1. Convert from Meters to Feet")
    print("2. Convert from Feet to Meters")
    conversion_type = get_user_input("Enter your choice: ")
    if conversion_type == '1':
        meters = float(get_user_input("Enter the length in meters: "))
        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet} feet")
    elif conversion_type == '2':
        feet = float(get_user_input("Enter the length in feet: "))
        meters = feet_to_meters(feet)
        print(f"{feet} feet is equal to {meters} meters")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def perform_weight_conversion():
    print("\nWeight Converter")
    print("1. Convert from Kilograms to Pounds")
    print("2. Convert from Pounds to Kilograms")
    conversion_type = get_user_input("Enter your choice: ")
    if conversion_type == '1':
        kilograms = float(get_user_input("Enter the weight in kilograms: "))
        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} kilograms is equal to {pounds} pounds")
    elif conversion_type == '2':
        pounds = float(get_user_input("Enter the weight in pounds: "))
        kilograms = pounds_to_kilograms(pounds)
        print(f"{pounds} pounds is equal to {kilograms} kilograms")
    else:
        print("Invalid choice. Please enter 1 or 2.")

def main():
    print("Welcome to the Unit Converter!")
    print("This program allows you to convert between different units of measurement.")

    while True:
        display_menu()
        choice = get_user_input("Enter your choice: ")

        if choice == '1':
            perform_temperature_conversion()
        elif choice == '2':
            perform_length_conversion()
        elif choice == '3':
            perform_weight_conversion()
        elif choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


# 
