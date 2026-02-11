"""
Pipeline-based Training Script for Traffic Volume Prediction
Uses sklearn Pipeline + ColumnTransformer for robust preprocessing
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import os
import warnings

warnings.filterwarnings('ignore')

print("=" * 80)
print("TRAFFIC VOLUME PREDICTION - PIPELINE-BASED TRAINING")
print("=" * 80)

# ============================================================================
# STEP 1: LOAD AND PREPARE DATA
# ============================================================================

print("\n[1/6] Loading data...")
df = pd.read_csv('datafile.csv')
print(f"Original data shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Remove duplicates
print("[1/6] Removing duplicates...")
initial_length = len(df)
df.drop_duplicates(inplace=True)
print(f"Removed {initial_length - len(df)} duplicate rows")

# ============================================================================
# STEP 2: FEATURE ENGINEERING
# ============================================================================

print("\n[2/6] Performing feature engineering...")

# Parse date_time
df['date_time'] = pd.to_datetime(df['date_time'], format='%d-%m-%Y %H:%M')
df['day'] = df['date_time'].dt.day_name()
df['month'] = df['date_time'].dt.month
df['year'] = df['date_time'].dt.year
df['hour'] = df['date_time'].dt.hour
df.drop('date_time', axis=1, inplace=True)

# Drop weather_description (redundant with weather_main)
df.drop('weather_description', axis=1, inplace=True)

print(f"Data shape after feature engineering: {df.shape}")
print(f"Columns: {list(df.columns)}")

# ============================================================================
# STEP 3: IDENTIFY CATEGORICAL AND NUMERICAL COLUMNS
# ============================================================================

print("\n[3/6] Identifying column types...")

# Separate target from features
X = df.drop('traffic_volume', axis=1)
y = df['traffic_volume']

# Identify categorical and numerical columns
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()

print(f"Categorical columns: {categorical_cols}")
print(f"Numerical columns: {numerical_cols}")

# ============================================================================
# STEP 4: SPLIT DATA
# ============================================================================

print("\n[4/6] Splitting data (85% train, 15% test)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.85, shuffle=True, random_state=42
)
print(f"Training set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# ============================================================================
# STEP 5: BUILD PIPELINES WITH PREPROCESSING
# ============================================================================

print("\n[5/6] Building preprocessing + model pipelines...")

# Create the preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_cols),
        ('num', StandardScaler(), numerical_cols)
    ]
)

# Define models
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree': DecisionTreeRegressor(random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

# Build and train pipelines
pipelines = {}
results = []

for model_name, model in models.items():
    print(f"\n  Training {model_name}...")
    
    # Create pipeline: preprocessing + model
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model)
    ])
    
    # Train
    pipeline.fit(X_train, y_train)
    pipelines[model_name] = pipeline
    
    # Evaluate
    y_pred_train = pipeline.predict(X_train)
    y_pred_test = pipeline.predict(X_test)
    
    train_mse = mean_squared_error(y_train, y_pred_train)
    train_r2 = r2_score(y_train, y_pred_train)
    train_mae = mean_absolute_error(y_train, y_pred_train)
    
    test_mse = mean_squared_error(y_test, y_pred_test)
    test_r2 = r2_score(y_test, y_pred_test)
    test_mae = mean_absolute_error(y_test, y_pred_test)
    
    results.append({
        'Model': model_name,
        'Train MSE': train_mse,
        'Test MSE': test_mse,
        'Train R²': train_r2,
        'Test R²': test_r2,
        'Train MAE': train_mae,
        'Test MAE': test_mae
    })
    
    print(f"    Train MSE: {train_mse:,.2f} | Test MSE: {test_mse:,.2f}")
    print(f"    Train R²:  {train_r2:.4f}   | Test R²:  {test_r2:.4f}")

# ============================================================================
# STEP 6: SAVE MODELS
# ============================================================================

print("\n[6/6] Saving pipeline models...")

# Save each pipeline
for model_name, pipeline in pipelines.items():
    file_path = f"{model_name} Pipeline.pkl"
    joblib.dump(pipeline, file_path)
    print(f"  ✓ Saved: {file_path}")

# Also save the preprocessor separately for reference
joblib.dump(preprocessor, "preprocessor.pkl")
print(f"  ✓ Saved: preprocessor.pkl")

# Save the feature information
feature_info = {
    'categorical_cols': categorical_cols,
    'numerical_cols': numerical_cols,
    'all_cols': categorical_cols + numerical_cols
}
joblib.dump(feature_info, "feature_info.pkl")
print(f"  ✓ Saved: feature_info.pkl")

# ============================================================================
# EVALUATION SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("EVALUATION SUMMARY")
print("=" * 80)

results_df = pd.DataFrame(results)
print("\n" + results_df.to_string(index=False))

# Find best models
best_test_r2_model = results_df.loc[results_df['Test R²'].idxmax(), 'Model']
best_test_mse_model = results_df.loc[results_df['Test MSE'].idxmin(), 'Model']

print("\n" + "=" * 80)
print(f"✓ Best Model (R² Score): {best_test_r2_model}")
print(f"✓ Best Model (MSE):      {best_test_mse_model}")
print("=" * 80)

# ============================================================================
# TEST PREDICTIONS WITH RAW INPUT
# ============================================================================

print("\n" + "=" * 80)
print("TESTING PREDICTIONS WITH RAW INPUT")
print("=" * 80)

# Test with sample raw input (no manual encoding needed!)
print("\nTesting with sample data (raw input, no manual encoding):")
sample_raw = X_test.iloc[:3].copy()

print("\nSample raw input:")
print(sample_raw)

print("\nActual values:")
print(y_test.iloc[:3].values)

print("\nPredictions from pipelines:")
for model_name, pipeline in pipelines.items():
    predictions = pipeline.predict(sample_raw)
    print(f"\n{model_name}:")
    for i, pred in enumerate(predictions):
        print(f"  Sample {i+1}: {pred:,.0f} vehicles")

print("\n" + "=" * 80)
print("TRAINING COMPLETE!")
print("=" * 80)
print("\nNext steps:")
print("1. Dashboard will now load pipeline models (e.g., 'Linear Regression Pipeline.pkl')")
print("2. Accept raw user input (with categorical values)")
print("3. Pipeline automatically handles preprocessing and prediction")
print("4. No manual feature alignment needed!")
print("=" * 80)
