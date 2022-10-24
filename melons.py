# Importing Pretty print for optimized terminal ouput
from pprint import pprint
# importing the csv files to melons.py
import csv

# Main Class (Melon)


class Melon:
    # Defining the main Class with Instances
    def __init__(self, melon_id, common_name, price, image_url, color, seedless):
        self.melon_id = melon_id
        self.common_name = common_name
        self.price = price
        self.image_url = image_url
        self.color = color
        self.seedless = seedless

    # Using a __repr__() to change the object memory to a string
    def __repr__(self):
        return f"<Melon: {self.melon_id}, {self.common_name}>"


# Empty dictionary to use with the function below to convert strings.
melon_dict = {}

# Function using DictReader to print the csv file.
with open("melons.csv") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        melon_id = row["melon_id"]

        melon = Melon(melon_id, row["common_name"], float(
            row["price"]), row["image_url"], row["color"], eval(row["seedless"]))

        melon_dict[melon_id] = melon

# Using pretty print import to list the melon dictionary
pprint(melon_dict)
