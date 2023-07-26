#!/usr/local/bin/python3
import math

def create_diurnal_data():
    # Number of data points for each minute in a day (24 hours * 60 minutes)
    num_data_points = 24 * 60

    # List to store the diurnal data series
    diurnal_data = []

    # Generate random data points with sine function modulation
    for minute in range(num_data_points):
        # Using a sine function to get higher values during working hours (9-5)
        value = 50 + 50 * math.sin((minute - 6 * 60) * (2 * math.pi) / (24 * 60))
        # Round the value to two decimal places
        rounded_value = round(value, 2)
        diurnal_data.append(rounded_value)

    return diurnal_data

if __name__ == "__main__":
    diurnal_data_series = create_diurnal_data()
    print(diurnal_data_series)

