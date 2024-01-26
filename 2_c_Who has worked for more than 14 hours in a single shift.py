# 2. c) Who has worked for more than 14 hours in a single shift
import pandas as pd
from datetime import timedelta

df = pd.read_csv('Assignment_Timecard.xlsx - Sheet1.csv')

# Convert 'Time' and 'Time Out' columns to datetime objects
df['Time'] = pd.to_datetime(df['Time'])
df['Time Out'] = pd.to_datetime(df['Time Out'])

# Calculate the duration of each shift
df['Shift Duration'] = df['Time Out'] - df['Time']

# Filter employees who have worked for more than 14 hours in a single shift
filtered_df = df[df['Shift Duration'] > timedelta(hours=14)]

# Get the unique names and positions of employees who meet the criteria
result = filtered_df[['Employee Name', 'Position ID']].drop_duplicates()

# result
print(result.to_string())
