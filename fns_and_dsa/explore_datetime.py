# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    """
    Calculate the future date after adding a specified number of days to the current date.

    Parameters:
    days (int): The number of days to add to the current date.

    Returns:
    future_date (datetime): The future date after adding the specified number of days.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date after {days} days: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()
