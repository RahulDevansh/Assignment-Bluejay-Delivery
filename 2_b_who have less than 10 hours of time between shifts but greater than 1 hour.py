# 2. b) who have less than 10 hours of time between shifts but greater than 1 hour
import pandas as pd
from datetime import timedelta

df = pd.read_csv('Assignment_Timecard.xlsx - Sheet1.csv')
# Convert 'Time' and 'Time Out' columns to datetime objects
df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

# Sort the DataFrame by 'Employee Name' and 'Time'
df.sort_values(['Employee Name', 'Time'], inplace=True)

# Calculate the time difference between consecutive shifts
df['Time Difference'] = df.groupby('Employee Name')['Time'].diff()

# Filter employees who have less than 10 hours but greater than 1 hour
filtered_df = df[(df['Time Difference'] > timedelta(hours=1)) & (df['Time Difference'] < timedelta(hours=10))]

# Get the unique names and positions of employees who meet the criteria
result = filtered_df[['Employee Name', 'Position ID']].drop_duplicates()

# result
print(result.to_string())
