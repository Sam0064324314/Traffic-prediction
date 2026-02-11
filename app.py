"""
Traffic Volume Prediction Dashboard
A production-quality interactive machine learning dashboard for traffic volume prediction.

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))

from utils import (
    load_model,
    load_all_models,
    calculate_metrics,
    calculate_residuals,
    plot_actual_vs_predicted,
    plot_residuals,
    plot_actual_vs_predicted_line,
    plot_model_comparison,
    plot_error_distribution,
    plot_feature_importance,
    get_feature_stats,
    get_feature_names
)


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Traffic Volume Prediction Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .section-header {
        border-bottom: 3px solid #1f77b4;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# INITIALIZATION & UTILITIES
# ============================================================================

def load_data():
    """
    Load test data with RAW categorical features (not one-hot encoded).
    
    The pipeline will automatically handle:
    - holiday: NaN or categorical values
    - weather_main: categorical values (Clouds, Rain, Clear, etc.)
    - day: day names (Monday, Tuesday, etc.)
    
    Returns:
        DataFrame with raw features suitable for pipeline.predict()
    """
    try:
        # Load test data (RAW features, no manual one-hot encoding)
        df = pd.read_csv('test_data.csv')
        return df
    except FileNotFoundError:
        st.warning("⚠️ test_data.csv not found. Generating synthetic data...")
        # Generate synthetic data with RAW categorical features
        np.random.seed(42)
        n_samples = 200
        df = pd.DataFrame({
            'traffic_volume': np.random.randint(1000, 8000, n_samples),
            'holiday': np.random.choice([None, 'Holiday'], n_samples, p=[0.95, 0.05]),
            'temp': np.random.uniform(260, 310, n_samples),
            'rain_1h': np.random.exponential(0.5, n_samples),
            'snow_1h': np.random.exponential(0.2, n_samples),
            'clouds_all': np.random.randint(0, 100, n_samples),
            'weather_main': np.random.choice(['Clouds', 'Rain', 'Clear', 'Snow'], n_samples),
            'day': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], n_samples),
            'month': np.random.randint(1, 13, n_samples),
            'year': np.random.choice([2012, 2013, 2014, 2015, 2016], n_samples),
            'hour': np.random.randint(0, 24, n_samples)
        })
        return df


@st.cache_resource
def get_models():
    """Load all models."""
    model_names = ['Linear Regression', 'Decision Tree', 'Random Forest']
    return load_all_models(model_names)


def get_model_predictions(pipeline, X_features):
    """
    Get predictions from a pipeline model.
    
    Pipeline automatically handles:
    - OneHotEncoding of categorical features
    - StandardScaling of numerical features
    
    Args:
        pipeline: sklearn.pipeline.Pipeline object
        X_features: DataFrame with raw features (no manual encoding needed)
    
    Returns:
        numpy array of predictions
    """
    try:
        return pipeline.predict(X_features)
    except Exception as e:
        st.error(f"Error making predictions: {str(e)}")
        return None


def get_feature_importance(pipeline, feature_names):
    """
    Extract feature importance from the pipeline's underlying model.
    
    Handles both tree-based models (feature_importances_) and linear models (coef_).
    
    Args:
        pipeline: sklearn.pipeline.Pipeline object
        feature_names: List of original feature names
    
    Returns:
        Dictionary of {feature_name: importance_value}
    """
    importance_dict = {}
    try:
        # Extract the actual model from the pipeline
        if hasattr(pipeline, 'named_steps') and 'model' in pipeline.named_steps:
            model = pipeline.named_steps['model']
        else:
            model = pipeline
        
        # Get feature importance from the model
        if hasattr(model, 'feature_importances_'):
            # Tree-based models (Decision Tree, Random Forest)
            importances = model.feature_importances_
            importance_dict = dict(zip(feature_names, importances))
        elif hasattr(model, 'coef_'):
            # Linear models
            coefs = np.abs(model.coef_)
            importance_dict = dict(zip(feature_names, coefs))
    except Exception as e:
        st.warning(f"Could not extract feature importance: {str(e)}")
    
    return importance_dict


# ============================================================================
# MAIN DASHBOARD
# ============================================================================

def main():
    """Main dashboard function."""
    
    # Header
    st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>
    🚗 Traffic Volume Prediction Dashboard
    </h1>
    <p style='text-align: center; color: #666;'>
    Interactive ML Model Evaluation and Prediction System
    </p>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Load data and models
    with st.spinner("Loading models and data..."):
        test_data = load_data()
        models = get_models()
        
        # Prepare features
        X_test = test_data.drop('traffic_volume', axis=1)
        y_test = test_data['traffic_volume'].values
        feature_names = list(X_test.columns)
    
    if not all(models.values()):
        st.error("❌ Could not load all models. Please ensure .pkl files exist in the directory.")
        return
    
    # ========================================================================
    # SIDEBAR - NAVIGATION & SETTINGS
    # ========================================================================
    
    with st.sidebar:
        st.header("⚙️ Navigation & Settings")
        
        # Model Selection
        selected_model_name = st.selectbox(
            "Select Model",
            options=list(models.keys()),
            help="Choose which model to evaluate and use for predictions"
        )
        selected_model = models[selected_model_name]
        
        st.divider()
        
        # Dashboard Sections
        st.subheader("Dashboard Sections")
        show_evaluation = st.checkbox("📊 Model Evaluation", value=True)
        show_visualizations = st.checkbox("📈 Visualizations", value=True)
        show_comparison = st.checkbox("🔄 Model Comparison", value=True)
        show_predictions = st.checkbox("🎯 Make Predictions", value=True)
        show_insights = st.checkbox("💡 Data Insights", value=True)
        
        st.divider()
        
        # Model Info
        st.subheader("Model Information")
        st.metric("Selected Model", selected_model_name)
        st.metric("Model Type", type(selected_model).__name__)
        st.text(f"Training samples: {len(y_test)}")
    
    # Calculate predictions for selected model after sidebar is created
    y_pred = get_model_predictions(selected_model, X_test) if selected_model is not None else None
    
    # ========================================================================
    # SECTION 1: MODEL EVALUATION
    # ========================================================================
    
    if show_evaluation:
        st.markdown('<div class="section-header">📊 Model Evaluation Metrics</div>', unsafe_allow_html=True)
        
        if y_pred is not None:
            # Calculate metrics
            metrics = calculate_metrics(y_test, y_pred)
            
            # Display metrics in columns
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    "MSE",
                    f"{metrics['MSE']:,.0f}",
                    help="Mean Squared Error - Lower is better"
                )
            
            with col2:
                st.metric(
                    "RMSE",
                    f"{metrics['RMSE']:,.0f}",
                    help="Root Mean Squared Error"
                )
            
            with col3:
                st.metric(
                    "MAE",
                    f"{metrics['MAE']:,.0f}",
                    help="Mean Absolute Error - Lower is better"
                )
            
            with col4:
                st.metric(
                    "R² Score",
                    f"{metrics['R2 Score']:.4f}",
                    help="R² Score - Higher is better (max 1.0)"
                )
            
            # Additional statistics
            with st.expander("📋 Detailed Error Statistics"):
                residuals = calculate_residuals(y_test, y_pred)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Mean Error", f"{np.mean(residuals):,.2f}")
                    st.metric("Max Error", f"{np.max(np.abs(residuals)):,.2f}")
                
                with col2:
                    st.metric("Std Error", f"{np.std(residuals):,.2f}")
                    st.metric("Min Error", f"{np.min(np.abs(residuals)):,.2f}")
    
    # ========================================================================
    # SECTION 2: VISUALIZATIONS
    # ========================================================================
    
    if show_visualizations:
        st.markdown('<div class="section-header">📈 Visualization Panel</div>', unsafe_allow_html=True)
        
        if y_pred is not None:
            # Create tabs for different visualizations
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "Actual vs Predicted Line",
                "Scatter Plot",
                "Residual Plot",
                "Error Distribution",
                "Performance Comparison"
            ])
            
            with tab1:
                st.plotly_chart(
                    plot_actual_vs_predicted_line(y_test, y_pred, sample_size=100)
                )
            
            with tab2:
                st.plotly_chart(
                    plot_actual_vs_predicted(y_test, y_pred)
                )
            
            with tab3:
                st.plotly_chart(
                    plot_residuals(y_test, y_pred)
                )
            
            with tab4:
                residuals = calculate_residuals(y_test, y_pred)
                st.plotly_chart(
                    plot_error_distribution(residuals)
                )
            
            with tab5:
                # Show metrics comparison with other models
                all_metrics = {}
                for model_name, model in models.items():
                    pred = get_model_predictions(model, X_test)
                    if pred is not None:
                        all_metrics[model_name] = calculate_metrics(y_test, pred)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.plotly_chart(
                        plot_model_comparison(all_metrics, 'MSE')
                    )
                with col2:
                    st.plotly_chart(
                        plot_model_comparison(all_metrics, 'R2 Score')
                    )
    
    # ========================================================================
    # SECTION 3: MODEL COMPARISON
    # ========================================================================
    
    if show_comparison:
        st.markdown('<div class="section-header">🔄 Model Comparison</div>', unsafe_allow_html=True)
        
        # Calculate metrics for all models
        comparison_data = []
        for model_name, model in models.items():
            pred = get_model_predictions(model, X_test)
            if pred is not None:
                metrics = calculate_metrics(y_test, pred)
                comparison_data.append({
                    'Model': model_name,
                    'MSE': metrics['MSE'],
                    'RMSE': metrics['RMSE'],
                    'MAE': metrics['MAE'],
                    'R² Score': metrics['R2 Score']
                })
        
        if comparison_data:  # Only display if we have data
            comparison_df = pd.DataFrame(comparison_data)
            
            # Display comparison table
            st.dataframe(
                comparison_df.style.format({
                    'MSE': '{:,.0f}',
                    'RMSE': '{:,.0f}',
                    'MAE': '{:,.0f}',
                    'R² Score': '{:.4f}'
                })
            )
            
            # Best performing models
            col1, col2, col3 = st.columns(3)
            with col1:
                best_mse = comparison_df.loc[comparison_df['MSE'].idxmin()]
                st.info(f"**Lowest MSE:** {best_mse['Model']}\n{best_mse['MSE']:,.0f}")
            
            with col2:
                best_mae = comparison_df.loc[comparison_df['MAE'].idxmin()]
                st.info(f"**Lowest MAE:** {best_mae['Model']}\n{best_mae['MAE']:,.0f}")
            
            with col3:
                best_r2 = comparison_df.loc[comparison_df['R² Score'].idxmax()]
                st.success(f"**Highest R² Score:** {best_r2['Model']}\n{best_r2['R² Score']:.4f}")
        else:
            st.warning("⚠️ Could not generate comparison data. Check if models can make predictions.")
    
    # ========================================================================
    # SECTION 4: PREDICTION INTERFACE
    # ========================================================================
    
    if show_predictions:
        st.markdown('<div class="section-header">🎯 Make Predictions</div>', unsafe_allow_html=True)
        
        st.write("""
        Adjust raw feature values below to get traffic volume predictions.
        The pipeline automatically handles categorical encoding internally!
        """)
        
        # Create input columns for numerical features
        numerical_features = X_test.select_dtypes(include=[np.number]).columns.tolist()
        categorical_features = X_test.select_dtypes(include=['object']).columns.tolist()
        
        user_input = {}
        test_data_sample = X_test.iloc[0]
        
        # --- NUMERICAL FEATURES ---
        st.subheader("📊 Numerical Features")
        pred_col1, pred_col2, pred_col3 = st.columns(3)
        col_idx = 0
        cols = [pred_col1, pred_col2, pred_col3]
        
        for feature in numerical_features:
            col = cols[col_idx % 3]
            with col:
                min_val = float(X_test[feature].min())
                max_val = float(X_test[feature].max())
                default_val = float(test_data_sample[feature])
                
                # Handle edge case where min == max
                if min_val == max_val:
                    # If all values are the same, add small range
                    max_val = min_val + 1.0
                    default_val = min_val
                
                # Calculate step size, ensuring it's not zero
                step_size = max(0.01, (max_val - min_val) / 100)
                
                user_input[feature] = st.slider(
                    f"{feature}",
                    min_value=min_val,
                    max_value=max_val,
                    value=min(max_val, max(min_val, default_val)),  # Clamp default to valid range
                    step=step_size,
                    format="%.2f"
                )
            col_idx += 1
        
        # --- CATEGORICAL FEATURES ---
        if categorical_features:
            st.subheader("🏷️ Categorical Features")
            cat_col1, cat_col2, cat_col3 = st.columns(3)
            cat_idx = 0
            cat_cols = [cat_col1, cat_col2, cat_col3]
            
            for feature in categorical_features:
                col = cat_cols[cat_idx % 3]
                with col:
                    unique_values = [None] + sorted(X_test[feature].dropna().unique().tolist())
                    default_idx = 0
                    if pd.notna(test_data_sample[feature]):
                        try:
                            default_idx = unique_values.index(test_data_sample[feature])
                        except ValueError:
                            default_idx = 0
                    
                    user_input[feature] = st.selectbox(
                        f"{feature}",
                        options=unique_values,
                        index=default_idx,
                        help=f"Select a value for {feature} (None = NaN)"
                    )
                cat_idx += 1
        
        # Prediction button
        if st.button("🔮 Predict Traffic Volume"):
            # Prepare input DataFrame with raw values (NO manual encoding)
            input_df = pd.DataFrame([user_input])
            
            # Pipeline automatically handles:
            # 1. OneHotEncoding of categorical features
            # 2. StandardScaling of numerical features
            # 3. Model prediction
            prediction = get_model_predictions(selected_model, input_df)
            
            if prediction is not None:
                st.divider()
                
                # Display prediction
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.subheader("📌 Prediction Result")
                    st.metric(
                        f"Predicted Traffic Volume ({selected_model_name})",
                        f"{prediction[0]:,.0f} vehicles",
                        help="Model prediction for the given input features"
                    )
                
                with col2:
                    # Get confidence based on R2 score
                    metrics = calculate_metrics(y_test, get_model_predictions(selected_model, X_test))
                    confidence = max(0, metrics['R2 Score'] * 100)
                    st.metric(
                        "Model Confidence",
                        f"{confidence:.1f}%",
                        help="Based on R² score"
                    )
                
                # Show prediction characteristics
                st.divider()
                st.write("**Prediction Characteristics:**")
                
                char_col1, char_col2, char_col3 = st.columns(3)
                with char_col1:
                    st.info(f"Min test value: {y_test.min():,.0f}")
                with char_col2:
                    st.info(f"Max test value: {y_test.max():,.0f}")
                with char_col3:
                    st.info(f"Mean test value: {y_test.mean():,.0f}")
    
    # ========================================================================
    # SECTION 5: DATA INSIGHTS
    # ========================================================================
    
    if show_insights:
        st.markdown('<div class="section-header">💡 Data Insights & Feature Importance</div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs([
            "Feature Importance",
            "Feature Statistics",
            "Target Variable Analysis"
        ])
        
        with tab1:
            st.subheader("🎯 Feature Importance")
            
            importance_dict = get_feature_importance(selected_model, feature_names)
            
            if importance_dict:
                st.plotly_chart(
                    plot_feature_importance(importance_dict, top_n=15)
                )
                
                # Show importance values in table
                with st.expander("📊 Feature Importance Values"):
                    importance_df = pd.DataFrame([
                        {'Feature': k, 'Importance': v}
                        for k, v in sorted(importance_dict.items(), key=lambda x: x[1], reverse=True)
                    ])
                    st.dataframe(
                        importance_df.style.format({'Importance': '{:.6f}'})
                    )
            else:
                st.info("Feature importance not available for this model")
        
        with tab2:
            st.subheader("📈 Feature Statistics")
            
            # Display feature statistics
            stats = X_test.describe().T
            st.dataframe(
                stats.style.format('{:.2f}')
            )
        
        with tab3:
            st.subheader("🎯 Target Variable (Traffic Volume) Analysis")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Mean", f"{y_test.mean():,.0f}")
            with col2:
                st.metric("Median", f"{np.median(y_test):,.0f}")
            with col3:
                st.metric("Std Dev", f"{y_test.std():,.0f}")
            with col4:
                st.metric("Count", f"{len(y_test)}")
            
            # Distribution plot
            import plotly.graph_objects as go
            fig = go.Figure(data=[
                go.Histogram(x=y_test, nbinsx=30, marker_color='rgba(31, 119, 180, 0.7)')
            ])
            fig.update_layout(
                title="Traffic Volume Distribution",
                xaxis_title="Traffic Volume",
                yaxis_title="Frequency",
                template='plotly_white',
                height=400
            )
            st.plotly_chart(fig)
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
    <p><strong>Traffic Volume Prediction Dashboard v1.0</strong></p>
    <p>A production-quality machine learning evaluation and prediction system</p>
    <p style='font-size: 0.85em;'>Built with Streamlit | Powered by Scikit-learn & Plotly</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
