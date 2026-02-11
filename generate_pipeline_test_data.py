"""
Generate test_data.csv from original data without manual one-hot encoding
Uses raw categorical values for pipeline-based predictions
"""

import pandas as pd
import joblib

# Load the original processed data
df = pd.read_csv('datafile.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Feature engineering (same as training)
df['date_time'] = pd.to_datetime(df['date_time'], format='%d-%m-%Y %H:%M')
df['day'] = df['date_time'].dt.day_name()
df['month'] = df['date_time'].dt.month
df['year'] = df['date_time'].dt.year
df['hour'] = df['date_time'].dt.hour
df.drop('date_time', axis=1, inplace=True)
df.drop('weather_description', axis=1, inplace=True)

# Save 200 random samples as test_data (with raw categorical values)
test_data = df.sample(n=200, random_state=42).reset_index(drop=True)

# Reorder columns to match training: target first, then features
cols = ['traffic_volume'] + [c for c in test_data.columns if c != 'traffic_volume']
test_data = test_data[cols]

# Save to CSV
test_data.to_csv('test_data.csv', index=False)
print(f"✓ Created test_data.csv with {len(test_data)} samples")
print(f"Columns: {list(test_data.columns)}")
print(f"\nFirst few rows:")
print(test_data.head())
