"""
Visualization utilities for the ML dashboard.
"""

import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from typing import Tuple, List


def plot_actual_vs_predicted(y_true: np.ndarray, y_pred: np.ndarray) -> go.Figure:
    """
    Create a scatter plot of actual vs predicted values.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Plotly figure object
    """
    fig = go.Figure()
    
    # Add scatter plot
    fig.add_trace(go.Scatter(
        x=y_true,
        y=y_pred,
        mode='markers',
        marker=dict(
            size=6,
            color='rgba(100, 149, 237, 0.6)',
            line=dict(color='rgba(100, 149, 237, 1)', width=1)
        ),
        name='Predictions'
    ))
    
    # Add perfect prediction line
    min_val = min(y_true.min(), y_pred.min())
    max_val = max(y_true.max(), y_pred.max())
    fig.add_trace(go.Scatter(
        x=[min_val, max_val],
        y=[min_val, max_val],
        mode='lines',
        line=dict(color='rgba(255, 99, 71, 0.8)', width=2, dash='dash'),
        name='Perfect Prediction'
    ))
    
    fig.update_layout(
        title='Actual vs Predicted Values',
        xaxis_title='Actual Traffic Volume',
        yaxis_title='Predicted Traffic Volume',
        hovermode='closest',
        template='plotly_white',
        height=500,
        showlegend=True
    )
    
    return fig


def plot_residuals(y_true: np.ndarray, y_pred: np.ndarray) -> go.Figure:
    """
    Create a residual plot for error analysis.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
    
    Returns:
        Plotly figure object
    """
    residuals = y_true - y_pred
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=y_pred,
        y=residuals,
        mode='markers',
        marker=dict(
            size=6,
            color='rgba(144, 238, 144, 0.6)',
            line=dict(color='rgba(144, 238, 144, 1)', width=1)
        ),
        name='Residuals'
    ))
    
    # Add zero line
    fig.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Zero Error")
    
    fig.update_layout(
        title='Residual Plot',
        xaxis_title='Predicted Values',
        yaxis_title='Residuals (Actual - Predicted)',
        hovermode='closest',
        template='plotly_white',
        height=500,
        showlegend=True
    )
    
    return fig


def plot_actual_vs_predicted_line(y_true: np.ndarray, y_pred: np.ndarray, sample_size: int = 100) -> go.Figure:
    """
    Create a line plot comparing actual vs predicted values over samples.
    
    Args:
        y_true: Actual values
        y_pred: Predicted values
        sample_size: Number of samples to plot
    
    Returns:
        Plotly figure object
    """
    indices = np.arange(min(sample_size, len(y_true)))
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=indices,
        y=y_true[:sample_size],
        mode='lines+markers',
        name='Actual',
        line=dict(color='rgba(31, 119, 180, 0.8)', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=indices,
        y=y_pred[:sample_size],
        mode='lines+markers',
        name='Predicted',
        line=dict(color='rgba(255, 127, 14, 0.8)', width=2)
    ))
    
    fig.update_layout(
        title=f'Actual vs Predicted (First {sample_size} Samples)',
        xaxis_title='Sample Index',
        yaxis_title='Traffic Volume',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    return fig


def plot_model_comparison(metrics_dict: dict, metric_name: str = 'MSE') -> go.Figure:
    """
    Create a bar chart comparing models based on a given metric.
    
    Args:
        metrics_dict: Dictionary of {model_name: {metric_name: value}}
        metric_name: Which metric to compare (e.g., 'MSE', 'R2 Score')
    
    Returns:
        Plotly figure object
    """
    models = list(metrics_dict.keys())
    values = [metrics_dict[model].get(metric_name, 0) for model in models]
    
    # Color based on metric (lower is better for MSE/RMSE/MAE, higher is better for R2)
    is_better_higher = 'R2' in metric_name
    colors = ['rgba(46, 204, 113, 0.7)' if (is_better_higher and v == max(values)) or (not is_better_higher and v == min(values)) 
              else 'rgba(52, 152, 219, 0.7)' for v in values]
    
    fig = go.Figure(data=[
        go.Bar(
            x=models,
            y=values,
            marker=dict(color=colors),
            text=[f'{v:,.2f}' for v in values],
            textposition='auto'
        )
    ])
    
    fig.update_layout(
        title=f'Model Comparison - {metric_name}',
        xaxis_title='Model',
        yaxis_title=metric_name,
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    return fig


def plot_error_distribution(residuals: np.ndarray) -> go.Figure:
    """
    Create a histogram of residual distribution.
    
    Args:
        residuals: Array of residuals
    
    Returns:
        Plotly figure object
    """
    fig = go.Figure(data=[
        go.Histogram(
            x=residuals,
            nbinsx=30,
            marker=dict(color='rgba(100, 149, 237, 0.7)'),
            name='Residuals'
        )
    ])
    
    fig.update_layout(
        title='Residual Distribution',
        xaxis_title='Residual Value',
        yaxis_title='Frequency',
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    return fig


def plot_feature_importance(importances: dict, top_n: int = 10) -> go.Figure:
    """
    Create a bar chart of feature importances.
    
    Args:
        importances: Dictionary of {feature_name: importance_value}
        top_n: Number of top features to display
    
    Returns:
        Plotly figure object
    """
    sorted_features = sorted(importances.items(), key=lambda x: x[1], reverse=True)[:top_n]
    feature_names = [f[0] for f in sorted_features]
    importance_values = [f[1] for f in sorted_features]
    
    fig = go.Figure(data=[
        go.Bar(
            y=feature_names,
            x=importance_values,
            orientation='h',
            marker=dict(color='rgba(155, 89, 182, 0.7)')
        )
    ])
    
    fig.update_layout(
        title=f'Top {top_n} Feature Importances',
        xaxis_title='Importance Score',
        yaxis_title='Feature',
        template='plotly_white',
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig
