# explore_datetime.py

import datetime


# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time using datetime.now()
    current_datetime = datetime.datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Display the formatted current date and time
    print(f"Current Date and Time: {formatted_datetime}")


# Part 2: Calculate a Future Date
def calculate_future_date():
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Get the current date using datetime.now()
    current_date = datetime.datetime.now().date()

    # Calculate the future date by adding the specified number of days
    future_date = current_date + datetime.timedelta(days=days_to_add)

    # Print the future date in the format "YYYY-MM-DD"
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")


# Calling the functions to demonstrate their functionality
if __name__ == "__main__":
    # Display current date and time
    display_current_datetime()

    # Calculate and display a future date
    calculate_future_date()
