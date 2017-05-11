europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }

# for key, value in europe.items():       # Dict uses method .items() or .iteritems() to loop over
#     print ("the capital of " + str(key) + " is " + value)

import numpy as np

# for i in np.nditer(numpy_2d_array):   # Numpy 2D array uses nd.iter function
#     print i

""" Looping on Pandas uses DataFraeName.iterrows() function"""
""" This takes two argument, say, lab, row"""
""" lab is the Label of the row and the row is Entire data of the row"""

Countries = ["Brazil", "Russia", "India", "China", "South Africa"]
Capital = ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"]
Area = [8.516, 17.100, 3.286, 9.597, 1.221]
Population = [200.40, 143.50, 1252.00, 1357.00, 52.98]
Labels = ["BR", "RU", "IN", "CH", "SA"]

my_dict = {
    "country":Countries,
    "capital":Capital,
    "area": Area,
    "population": Population
}

import pandas as pd

brics = pd.DataFrame(my_dict)
brics.index = Labels

# for lab, row in brics.iterrows():
#     print lab + ": " + row["capital"]

for lab, row in brics.iterrows():
    brics.loc[lab, "name_length"] = len(row["country"])

#print(brics)

""""Another method to add a column and fill in values with looping"""

brics["new_column"] = brics["country"].apply(len)

#print(brics)


names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt'] # The country names for which data is available.
dr =  [True, False, False, False, True, True, True] # A list with booleans that tells whether people drive left or right in the corresponding country.
cpc = [809, 731, 588, 18, 200, 70, 45] # The number of motor vehicles per 1000 people in the correspon
# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country":names, "drives_right":dr, "cars_per_cap":cpc}
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
# Specify the row labels
cars.index = row_labels

for lab, row in cars.iterrows():
    print(lab + ": " + str(row["cars_per_cap"]))

# for lab, row in cars.iterrows():
#     cars.loc[lab, "COUNTRY"] = row["country"].upper()
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)

