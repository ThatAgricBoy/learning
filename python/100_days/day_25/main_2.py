"""using readlines() to access the weather data"""
# with open("./weather_data.csv") as data_file:
#     for lines in data:
#         data = data_file.readlines()
"""
#     using the comma separated values(csv) format to acces thw
#     weather data
# """
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# temperature_list = data["temp"].to_list()
#
# """finding the mean using python"""
# average_temp = sum(temperature_list)/len(temperature_list)
# print(round(average_temp, 2))
#
# """finding the mean using pandas"""
# print(data["temp"].mean())
# print(data["temp"].max())
#
# """getting the temperature of a particular day"""
# print(data[data.day == "monday"])
#
# """getting the maximum temp for the week"""
# print(data[data.temp == data["temp"].max()])
#
# """creating a data frame from scratch"""
# data_dict = {
#     "students": ["Ayo", "Seyi", "Max"],
#     "scores": [78, 85, 90]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")

import pandas
data = pandas.read_csv("squirrel_count.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("color_counts_of_squirrels")