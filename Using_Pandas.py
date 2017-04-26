import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] # The country names for which data is available.
dr =  [True, False, False, False, True, True, True] # A list with booleans that tells whether people drive left or right in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45] # The number of motor vehicles per 1000 people in the corresponding country.


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names, "drives_right":dr, "cars_per_cap":cpc}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']


# Specify the row labels
cars.index = row_labels
print(cars)


# The data is available in a CSV file, named cars.csv
# Import CSV files and make the column 0 as the index or row label
cars = pd.read_csv("cars.csv", index_col=0)
print(cars)



