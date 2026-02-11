"""
Script to generate sample test data for the dashboard.
Run this script to create test_data.csv which will be used by the dashboard.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def generate_test_data():
    """
    Generate sample test data mimicking the traffic volume dataset structure.
    """
    # Read the original data to understand its structure
    try:
        df = pd.read_csv('datafile.csv')
    except FileNotFoundError:
        print("Creating synthetic test data...")
        # Create synthetic data if original is not available
        np.random.seed(42)
        n_samples = 200
        
        df = pd.DataFrame({
            'traffic_volume': np.random.randint(1000, 8000, n_samples),
            'holiday_none': np.random.choice([0, 1], n_samples),
            'holiday_holiday': np.random.choice([0, 1], n_samples),
            'temp': np.random.uniform(260, 310, n_samples),
            'rain_1h': np.random.exponential(0.5, n_samples),
            'snow_1h': np.random.exponential(0.2, n_samples),
            'clouds_all': np.random.randint(0, 100, n_samples),
            'weather_main_Clouds': np.random.choice([0, 1], n_samples),
            'weather_main_Rain': np.random.choice([0, 1], n_samples),
            'weather_main_Clear': np.random.choice([0, 1], n_samples),
            'day_Monday': np.random.choice([0, 1], n_samples),
            'day_Tuesday': np.random.choice([0, 1], n_samples),
            'day_Wednesday': np.random.choice([0, 1], n_samples),
            'day_Thursday': np.random.choice([0, 1], n_samples),
            'day_Friday': np.random.choice([0, 1], n_samples),
            'day_Saturday': np.random.choice([0, 1], n_samples),
            'day_Sunday': np.random.choice([0, 1], n_samples),
            'month': np.random.randint(1, 13, n_samples),
            'year': np.random.choice([2012, 2013, 2014, 2015, 2016], n_samples),
            'hour': np.random.randint(0, 24, n_samples)
        })
        return df
    
    # If we got here, we have the original data
    # Let's create test data from it
    X = df.drop('traffic_volume', axis=1)
    y = df['traffic_volume']
    
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Recreate the dataframe with predictions (will be overwritten by actual predictions)
    test_df = X_test.copy()
    test_df['traffic_volume'] = y_test.values
    
    return test_df


if __name__ == "__main__":
    test_data = generate_test_data()
    test_data.to_csv('test_data.csv', index=False)
    print(f"✓ Test data generated: test_data.csv ({len(test_data)} samples)")
    print(f"✓ Features: {list(test_data.columns)}")
