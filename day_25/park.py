import pandas as pd


# grey squirels
data = pd.read_csv("data.csv")
colors = data["Primary Fur Color"]

gray, cinnamon, black = 0, 0, 0

for i in colors:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        cinnamon += 1
    elif i == "Black":
        black += 1


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data = pd.DataFrame(data_dict)
data.to_csv("colors.csv")
