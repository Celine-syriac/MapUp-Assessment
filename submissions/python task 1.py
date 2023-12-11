#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


#1
def generate_car_matrix(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Create a pivot table using id_1 as index, id_2 as columns, and car as values
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')

    # Fill NaN values with 0 (diagonal values)
    car_matrix = car_matrix.fillna(0)

    return car_matrix

# Replace 'dataset-1.csv' with the actual path or URL to your CSV file
result_matrix = generate_car_matrix('dataset-1.csv')

# Display the resulting DataFrame
print(result_matrix)


# In[10]:


#2

def get_type_count(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Add a new categorical column 'car_type' based on the 'car' column values
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each 'car_type' category
    type_count = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_count = dict(sorted(type_count.items()))

    return sorted_type_count

# Replace 'dataset-1.csv' with the actual path or URL to your CSV file
result_type_count = get_type_count('dataset-1.csv')

# Display the resulting dictionary
print(result_type_count)


# In[12]:


#3

def get_bus_indexes(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Calculate the mean value of the 'bus' column
    bus_mean = df['bus'].mean()

    # Identify indices where the 'bus' values are greater than twice the mean value
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

# Replace 'dataset-1.csv' with the actual path or URL to your CSV file
result_bus_indexes = get_bus_indexes('dataset-1.csv')

# Display the resulting list of indices
print(result_bus_indexes)


# In[13]:


#4
def filter_routes(dataset):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset)

    # Filter routes based on the average of values in the 'truck' column
    filtered_routes = df.groupby('route')['truck'].mean().loc[lambda x: x > 7].index.tolist()

    # Sort the list of routes in ascending order
    filtered_routes.sort()

    return filtered_routes

# Replace 'dataset-1.csv' with the actual path or URL to your CSV file
result_filtered_routes = filter_routes('dataset-1.csv')

# Display the resulting sorted list of routes
print(result_filtered_routes)


# In[14]:


#5

def multiply_matrix(car_matrix):
    # Create a copy of the input DataFrame to avoid modifying the original
    modified_matrix = car_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Assuming result_matrix is the DataFrame obtained from generate_car_matrix
# Replace 'dataset-1.csv' with the actual path or URL to your CSV file
result_matrix = generate_car_matrix('dataset-1.csv')

# Apply the multiply_matrix function to the result_matrix
modified_result = multiply_matrix(result_matrix)

# Display the modified DataFrame
print(modified_result)


# In[ ]:




