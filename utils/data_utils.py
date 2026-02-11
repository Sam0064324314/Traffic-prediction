"""
Data processing and preparation utilities.
"""

import pandas as pd
import numpy as np
from typing import Tuple, List


def load_test_data(filepath: str) -> Tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    """
    Load test data from a CSV file.
    
    Args:
        filepath: Path to the test data file
    
    Returns:
        Tuple of (features DataFrame, actual values, feature names list)
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Test data file not found: {filepath}")


def get_feature_names(X: pd.DataFrame) -> List[str]:
    """
    Get the list of feature names from a DataFrame.
    
    Args:
        X: Features DataFrame
    
    Returns:
        List of feature names
    """
    return list(X.columns)


def get_feature_dtypes(X: pd.DataFrame) -> dict:
    """
    Get data types of features.
    
    Args:
        X: Features DataFrame
    
    Returns:
        Dictionary of {feature_name: dtype}
    """
    return X.dtypes.to_dict()


def get_feature_stats(X: pd.DataFrame) -> pd.DataFrame:
    """
    Get summary statistics for all features.
    
    Args:
        X: Features DataFrame
    
    Returns:
        DataFrame with summary statistics
    """
    return X.describe()


def prepare_sample_input(feature_values: dict, feature_names: List[str]) -> pd.DataFrame:
    """
    Prepare a sample input for prediction.
    
    Args:
        feature_values: Dictionary of {feature_name: value}
        feature_names: List of expected feature names
    
    Returns:
        DataFrame formatted for model prediction
    """
    # Create a DataFrame with a single row
    sample_data = {}
    for feature in feature_names:
        sample_data[feature] = [feature_values.get(feature, 0)]
    
    return pd.DataFrame(sample_data)


def validate_input(feature_values: dict, feature_stats: pd.DataFrame) -> Tuple[bool, str]:
    """
    Validate input values against data statistics.
    
    Args:
        feature_values: Dictionary of input values
        feature_stats: DataFrame with summary statistics
    
    Returns:
        Tuple of (is_valid, message)
    """
    for feature, value in feature_values.items():
        if feature in feature_stats.columns:
            min_val = feature_stats[feature]['min']
            max_val = feature_stats[feature]['max']
            
            if value < min_val or value > max_val:
                return False, f"{feature} value {value} is outside range [{min_val}, {max_val}]"
    
    return True, "All inputs are valid"


def get_categorical_features(X: pd.DataFrame) -> List[str]:
    """
    Get list of categorical features.
    
    Args:
        X: Features DataFrame
    
    Returns:
        List of categorical feature names
    """
    return X.select_dtypes(include=['object']).columns.tolist()


def get_numerical_features(X: pd.DataFrame) -> List[str]:
    """
    Get list of numerical features.
    
    Args:
        X: Features DataFrame
    
    Returns:
        List of numerical feature names
    """
    return X.select_dtypes(include=[np.number]).columns.tolist()
