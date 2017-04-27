import numpy as np
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] # The country names for which data is available.
dr =  [True, False, False, False, True, True, True] # A list with booleans that tells whether people drive left or right in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45] # The number of motor vehicles per 1000 people in the corresponding country.
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

my_dict = {
    "country":names,
    "drives_right":dr,
    "cars_per_cap":cpc
}

cars = pd.DataFrame(my_dict)
cars.index = row_labels
print(cars)
# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[cars["drives_right"]]
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc>500
car_maniac = cars[many_cars]
print(car_maniac)


# Create medium: observations with cars_per_cap between 100 and 500

medium = cars[np.logical_and(cars["cars_per_cap"]>100, cars["cars_per_cap"]<500)]

print(medium)
