#!/usr/local/bin/python3
import math

def create_diurnal_data():
    # Number of data points for each hour (24 hours in a day)
    num_data_points = 24

    # List to store the diurnal data series
    diurnal_data = []

    # Generate random data points with sine function modulation
    for hour in range(num_data_points):
        # Using a sine function to get higher values during working hours (9-5)
        value = 50 + 50 * math.sin((hour - 6) * (2 * math.pi) / 24)
        diurnal_data.append(value)

    return diurnal_data

if __name__ == "__main__":
    diurnal_data_series = create_diurnal_data()
    print(diurnal_data_series)

