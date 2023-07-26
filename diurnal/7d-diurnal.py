#!/usr/local/bin/python3
import math
def create_diurnal_data():
    # Number of data points for each minute in 7 days (7 days * 24 hours * 60 minutes)
    num_data_points = 7 * 24 * 60

    # List to store the diurnal data series
    diurnal_data = []

    # Generate random data points with sine function modulation
    for minute in range(num_data_points):
        # Convert the minute value to the corresponding hour of the week
        hour_of_week = (minute // 60) + 1  # Add 1 to make 1-based index (Monday is 1)

        # Using a sine function to get larger values during business hours (9-5) on weekdays
        if hour_of_week % 24 in range(9, 18) and hour_of_week % 168 not in range(144, 168):
            value = 50 + 50 * math.sin((minute - 9 * 60) * (2 * math.pi) / (7 * 24 * 60))
        else:
            # For non-business hours, use lower values
            value = 50 + 25 * math.sin((minute + 3 * 60) * (2 * math.pi) / (7 * 24 * 60))

        # Round the value to two decimal places
        rounded_value = round(value, 2)
        diurnal_data.append(rounded_value)

    return diurnal_data

if __name__ == "__main__":
    diurnal_data_series = create_diurnal_data()
    print(diurnal_data_series)

