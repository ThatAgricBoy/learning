"""using readlines() to access the weather data"""
# with open("./weather_data.csv") as data_file:
#     for lines in data:
#         data = data_file.readlines()
"""
    using the comma separated values(csv) format to acces thw
    weather data
"""
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])