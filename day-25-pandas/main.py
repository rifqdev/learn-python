# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')

# average = data["temp"].mean()
# max = data["temp"].max()
# print(max)

# get data in row
# print(data[data["temp"] == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create dataFrame from scracth
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")



# 2018_Central_Park_Squirrel_Census_-_Squirrel_Data
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

color_list = ["Gray", "Cinnamon", "Black"]
count_color = []
for color in color_list:
    len_data = len(data[data["Primary Fur Color"] == str(color)])
    count_color.append(len_data)


data_dict = {
    "Fur Color": color_list,
    "Count": count_color
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirell_count.csv")