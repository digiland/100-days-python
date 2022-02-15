# import csv

# with open("weather_data.csv") as data:
#     info = csv.reader(data)
#     temperature = []
#     for row in info:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

#     print(temperature)


import pandas as pd

data = pd.read_csv("weather_data.csv")

temps = data["temp"].max()
print(f"The average is {temps} ")
data["condition"]


print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

celsius = (monday.temp) * 9/5 + 32
print(celsius)


data_dict = {
    "students": ["Rolf", "Bob", "Jen", "Anne"],
    "grades": [87, 92, 77, 95]
}


data = pd.DataFrame(data_dict)
data.to_csv("grades.csv")
