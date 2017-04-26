import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] # The country names for which data is available.
dr =  [True, False, False, False, True, True, True] # A list with booleans that tells whether people drive left or right in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45] # The number of motor vehicles per 1000 people in the corresponding country.


# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names, "drives_right":dr, "cars_per_cap":cpc}


# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)


row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# Specify the row labels
cars.index = row_labels
print(cars)

print(cars["country"])
print(cars[["country"]])
print(cars[["country", "drives_right"]])

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


# LOC and ILOC (1):

# Print out observation for Japan
print(cars.loc[["JAP"]])
print(cars.iloc[[2]])

# Print out observations for Australia and Egypt
print(cars.loc[["AUS", "EG"]])
print(cars.iloc[[1, 6]])


# LOC and ILOC (2):

# Print out drives_right value of Morocco
print (cars.loc[["MOR"], ["drives_right"]])
print (cars.iloc[[5], [2]])

# Print sub-DataFrame
print (cars.loc[["RU", "MOR"], ["country", "drives_right"]])
print (cars.iloc[[4, 5], [1, 2]])

# LOC and ILOC (3):

# Print out drives_right column as Series
print (cars.loc[:, "drives_right"])
print (cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print (cars.loc[:, ["drives_right"]])
print (cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print (cars.loc[:, ["cars_per_cap", "drives_right"]])
print (cars.iloc[:, [0, 2]])