import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_data = data["Primary Fur Color"]

# get the counts
gray = len(data[data["Primary Fur Color"] == 'Gray'])
black = len(data[data["Primary Fur Color"] == 'Black'])
red = len(data[data["Primary Fur Color"] == 'Cinnamon'])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_fur_color_counts.csv")




