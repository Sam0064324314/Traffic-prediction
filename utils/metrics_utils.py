"""
Model evaluation metrics calculation utilities.
"""

import numpy as np
from typing import Tuple
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """
    Calculate comprehensive model evaluation metrics.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Dictionary containing MSE, MAE, and R2 Score
    """
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mse)
    
    return {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R2 Score': r2
    }


def calculate_residuals(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    """
    Calculate prediction residuals.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Array of residuals (errors)
    """
    return y_true - y_pred


def get_prediction_error_stats(residuals: np.ndarray) -> dict:
    """
    Get statistics about prediction errors.
    
    Args:
        residuals: Array of residuals
    
    Returns:
        Dictionary containing error statistics
    """
    return {
        'Mean Error': np.mean(residuals),
        'Std Error': np.std(residuals),
        'Max Error': np.max(np.abs(residuals)),
        'Min Error': np.min(np.abs(residuals))
    }


def format_metric(value: float, metric_name: str) -> str:
    """
    Format a metric value for display.
    
    Args:
        value: The metric value
        metric_name: Name of the metric
    
    Returns:
        Formatted string representation
    """
    if 'R2' in metric_name or 'Score' in metric_name:
        return f"{value:.4f}"
    else:
        return f"{value:,.2f}"
