# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# built - in
# import csv
# with open("weather_data.csv") as file:
#     # data is the object type
#     data = csv.reader(file)
#     temperature = []
#     # can iterate, first element is title
#     for row in data:
#         if row[1] != 'temp' and row[1] != None:
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# CONCEPT
# print(data)
# # list of the column - first row is the name of the column
# print(data["temp"])
# # data frame: whole table of data
# print(type(data))
# # series: the list of the column of data
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

# data["temp"] is the type series, after .to_list() it becomes a type list
temp_list = data["temp"].to_list()
print(temp_list)
# average
# sum = sum(temp_list)
# length = len(temp_list)
# average = round(sum / length, 2)
# print(average)
print(data["temp"].mean())
print(data["temp"].max())

# Get data in column
# Series - column - two ways
# name must match like dict
print(data['day'])
print(data.day)

#   Get data in row: data frame is data, condition is [data.day == "Monday"] to get the row
print(data[data.day == "Monday"])
# Get the data in row where the temp is the highest
print(data[data.temp == data.temp.max()])

# Get partial data from the row
monday = data[data.day == "Monday"]
print(monday.condition)
# Get Monday's temp from Celsius to Fahrenheit
mon = data[data.day == "Monday"]
fahrenheit = int(mon.temp)  * ( 9/ 5) + 32
print(fahrenheit)

# Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
excel_data = pandas.DataFrame(data_dict)
print(excel_data)
# create csv
excel_data.to_csv("new_data.csv")

