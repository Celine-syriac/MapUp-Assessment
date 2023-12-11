#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2
import pandas as pd

def unroll_distance_matrix(distance_matrix):
    # Use the melt function to unroll the distance matrix
    unrolled_df = distance_matrix.reset_index().melt(id_vars='index', var_name='id_end', value_name='distance')

    # Rename columns to match the desired output
    unrolled_df.columns = ['id_start', 'id_end', 'distance']

    # Filter out rows where id_start is equal to id_end
    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']]

    # Reset index and drop the old index column
    unrolled_df = unrolled_df.reset_index(drop=True)

    return unrolled_df



# In[ ]:


#3
import pandas as pd

def find_ids_within_ten_percentage_threshold(distance_df, reference_value):
    # Calculate the average distance for the reference value
    reference_avg_distance = distance_df[distance_df['id_start'] == reference_value]['distance'].mean()

    # Calculate the lower and upper thresholds within 10%
    lower_threshold = reference_avg_distance - (reference_avg_distance * 0.1)
    upper_threshold = reference_avg_distance + (reference_avg_distance * 0.1)

    # Filter the DataFrame based on the thresholds
    filtered_df = distance_df[
        (distance_df['id_start'] != reference_value) & 
        (distance_df['distance'] >= lower_threshold) & 
        (distance_df['distance'] <= upper_threshold)
    ]

    # Get the sorted list of values from the 'id_start' column
    result_list = sorted(filtered_df['id_start'].unique())

    return result_list



# In[ ]:


#4

def calculate_toll_rate(distance_df):
    # Create a copy of the input DataFrame to avoid modifying the original
    toll_rate_df = distance_df.copy()

    # Define rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Calculate toll rates for each vehicle type
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        toll_rate_df[vehicle_type] = toll_rate_df['distance'] * rate_coefficient

    return toll_rate_df

# Assuming unrolled_distance_df is the DataFrame obtained from unroll_distance_matrix
# Replace 'dataset-2.csv' with the actual path or URL to your CSV file
unrolled_distance_df = unroll_distance_matrix('dataset-2.csv')

# Apply the calculate_toll_rate function
result_toll_rate_df = calculate_toll_rate(unrolled_distance_df)

# Display the resulting DataFrame with added toll rate columns
print(result_toll_rate_df)


# In[ ]:




