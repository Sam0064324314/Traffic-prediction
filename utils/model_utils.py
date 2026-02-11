"""
Model loading and caching utilities for the ML dashboard.
Now loads sklearn Pipeline models that include preprocessing + model.
"""

import joblib
import streamlit as st
from pathlib import Path
from typing import Dict, Any


def get_model_path(model_name: str) -> str:
    """
    Get the file path for a given model pipeline.
    
    Note: Models are trained as sklearn.pipeline.Pipeline objects that include:
    - ColumnTransformer for preprocessing (OneHotEncoding + Scaling)
    - The actual model (LinearRegression, DecisionTree, or RandomForest)
    
    Args:
        model_name: Name of the model (e.g., 'Linear Regression')
    
    Returns:
        Full path to the pipeline model file
    """
    # Pipeline models are saved with " Pipeline.pkl" suffix
    model_file = f"{model_name} Pipeline.pkl"
    model_path = Path(__file__).parent.parent / model_file
    return str(model_path)


@st.cache_resource
def load_model(model_name: str) -> Any:
    """
    Load a trained pipeline model from disk with caching.
    
    The loaded pipeline includes:
    - Categorical preprocessing: OneHotEncoder(handle_unknown='ignore')
    - Numerical preprocessing: StandardScaler
    - Model: LinearRegression, DecisionTree, or RandomForest
    
    Usage:
        pipeline = load_model('Random Forest')
        prediction = pipeline.predict(raw_input_df)  # No manual encoding needed!
    
    Args:
        model_name: Name of the model to load
    
    Returns:
        Loaded sklearn.pipeline.Pipeline object
    """
    model_path = get_model_path(model_name)
    try:
        pipeline = joblib.load(model_path)
        return pipeline
    except FileNotFoundError:
        st.error(f"Model pipeline file not found: {model_path}")
        return None


def load_all_models(model_names: list) -> Dict[str, Any]:
    """
    Load multiple pipeline models at once.
    
    Args:
        model_names: List of model names to load
    
    Returns:
        Dictionary mapping model names to loaded pipeline objects
    """
    models = {}
    for model_name in model_names:
        models[model_name] = load_model(model_name)
    return models


def get_model_type(model) -> str:
    """
    Get the type/name of the actual ML model (from the pipeline).
    
    Args:
        model: The pipeline object
    
    Returns:
        String representation of the model type (e.g., 'RandomForestRegressor')
    """
    if model is None:
        return "Unknown"
    
    # For Pipeline objects, get the model from the last step
    try:
        if hasattr(model, 'named_steps') and 'model' in model.named_steps:
            actual_model = model.named_steps['model']
            return type(actual_model).__name__
    except:
        pass
    
    return type(model).__name__
