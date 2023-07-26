#!/usr/local/bin/python3
print("hello")

import random

def create_diurnal_data():
    # Number of data points for each hour (24 hours in a day)
    num_data_points = 24

    # List to store the diurnal data series
    diurnal_data = []

    # Generate random data points for each hour between 0 and 100
    for _ in range(num_data_points):
        data_point = random.randint(0, 100)
        diurnal_data.append(data_point)

    return diurnal_data

if __name__ == "__main__":
    diurnal_data_series = create_diurnal_data()
    print(diurnal_data_series)

