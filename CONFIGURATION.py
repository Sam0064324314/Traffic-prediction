"""
Configuration Guide for Traffic Volume Prediction Dashboard

This file documents all customization points and configuration options.
"""

# ============================================================================
# DASHBOARD CUSTOMIZATION GUIDE
# ============================================================================

"""
1. SIDEBAR CONFIGURATION
   Location: app.py, lines ~220-260
   
   Customize model selection:
   - Change model list in get_models()
   - Add new models: place .pkl in root directory
   - Update model_names list with new names
"""

MODELS = ['Linear Regression', 'Decision Tree', 'Random Forest']
# Add: MODELS = [..., 'Your New Model']


"""
2. METRICS CONFIGURATION
   Location: utils/metrics_utils.py
   
   Modify metric calculations:
   - Adjust error threshold values
   - Change metric formatting
   - Add custom metrics
"""

DEFAULT_METRICS = ['MSE', 'RMSE', 'MAE', 'R2 Score']


"""
3. VISUALIZATION CONFIGURATION
   Location: utils/plot_utils.py
   
   Customize plots:
   - Change colors: marker=dict(color='rgba(R, G, B, Alpha)')
   - Modify sizes: size=6, width=2
   - Update layouts: height=500, width=800
"""

# Color Scheme (Plotly Colors)
COLORS = {
    'primary': 'rgba(31, 119, 180, 0.8)',    # Blue
    'secondary': 'rgba(255, 127, 14, 0.8)',  # Orange
    'success': 'rgba(44, 160, 44, 0.8)',     # Green
    'danger': 'rgba(214, 39, 40, 0.8)',      # Red
    'info': 'rgba(100, 149, 237, 0.8)',      # Cornflower Blue
}


"""
4. DATA CONFIGURATION
   Location: utils/data_utils.py or prepare_test_data.py
   
   Modify data loading:
   - Change file paths
   - Add data validation
   - Transform features
"""

DATA_PATH = 'test_data.csv'
TRAIN_DATA_PATH = 'datafile.csv'
TARGET_COLUMN = 'traffic_volume'


"""
5. FEATURE CONFIGURATION
   Location: app.py, Prediction Interface section
   
   Customize prediction inputs:
   - Add/remove feature sliders
   - Change slider ranges
   - Set default values
"""

# Example: Adding new feature slider
# with st.slider('feature_name', min_value=0, max_value=100, value=50)


"""
6. UI/UX CUSTOMIZATION
   Location: app.py, top of file
   
   Modify appearance:
   - Page config: page_title, page_icon, layout
   - Custom CSS: st.markdown() calls
   - Theme colors in CSS
"""

PAGE_CONFIG = {
    'page_title': 'Traffic Volume Prediction Dashboard',
    'page_icon': '🚗',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded'
}


"""
7. SECTION VISIBILITY
   Location: app.py, sidebar, lines ~250-260
   
   Toggle dashboard sections:
   - show_evaluation: Boolean
   - show_visualizations: Boolean
   - show_comparison: Boolean
   - show_predictions: Boolean
   - show_insights: Boolean
"""

VISIBLE_SECTIONS = {
    'evaluation': True,
    'visualizations': True,
    'comparison': True,
    'predictions': True,
    'insights': True
}


"""
8. MODEL CONFIGURATION
   Location: utils/model_utils.py
   
   Modify model loading:
   - Change file locations
   - Add model validation
   - Implement custom loaders
"""

MODEL_EXTENSIONS = {
    'pkl': 'joblib',      # Standard scikit-learn models
    'h5': 'tensorflow',   # TensorFlow models
    'pt': 'pytorch'       # PyTorch models
}


"""
9. PLOTTING CONFIGURATION
   Location: utils/plot_utils.py
   
   Customize visualizations:
   - Plot dimensions: height, width
   - Template: 'plotly_white', 'plotly_dark'
   - Number of bins in histograms
   - Line styles: dash, solid
"""

PLOT_CONFIG = {
    'height': 500,
    'width': None,  # Auto
    'template': 'plotly_white',
    'hovermode': 'closest',
    'showlegend': True
}


"""
10. CACHING CONFIGURATION
    Location: app.py, utils/model_utils.py
    
    Optimize performance:
    - Cache resources: @st.cache_resource
    - Cache data: @st.cache_data
    - Control cache time-to-live (ttl)
"""

CACHE_CONFIG = {
    'resource_ttl': None,  # Cache indefinitely
    'data_ttl': 3600,      # 1 hour
}


# ============================================================================
# QUICK MODIFICATION EXAMPLES
# ============================================================================

"""
EXAMPLE 1: Change Dashboard Title
   File: app.py, line ~95
   
   Before:
   st.markdown('''<h1>Traffic Volume Prediction Dashboard</h1>''')
   
   After:
   st.markdown('''<h1>My Custom Title</h1>''')
"""


"""
EXAMPLE 2: Add New Model
   1. Train and save model: joblib.dump(model, 'MyModel.pkl')
   2. Update app.py line ~235: model_names.append('MyModel')
   3. Restart dashboard
"""


"""
EXAMPLE 3: Change Color Scheme
   File: utils/plot_utils.py
   
   Find: marker=dict(color='rgba(31, 119, 180, 0.6)')
   Change to: marker=dict(color='rgba(255, 99, 71, 0.6)')  # Red
"""


"""
EXAMPLE 4: Modify Prediction Features
   File: app.py, around line ~470
   
   Add new slider:
   user_input['new_feature'] = st.slider(
       'New Feature',
       min_value=0,
       max_value=100,
       value=50
   )
"""


"""
EXAMPLE 5: Hide Dashboard Section
   File: app.py, sidebar section
   
   Change: show_evaluation = st.checkbox("...", value=True)
   To: show_evaluation = st.checkbox("...", value=False)
"""


# ============================================================================
# RECOMMENDED CUSTOMIZATIONS FOR PRODUCTION
# ============================================================================

"""
🔒 SECURITY
   - Add authentication: streamlit-authenticator package
   - Validate all user inputs
   - Sanitize file paths
   - Use environment variables for sensitive data

⚡ PERFORMANCE
   - Implement result caching for predictions
   - Reduce plot complexity for large datasets
   - Use data sampling for visualizations
   - Enable compression for data transmission

📊 DATA
   - Add data validation on startup
   - Implement data quality checks
   - Log predictions for audit trails
   - Monitor model drift

🎨 DESIGN
   - Implement dark/light mode toggle
   - Add custom branding
   - Use consistent color scheme
   - Optimize for mobile devices

📈 MONITORING
   - Track prediction volume
   - Monitor prediction accuracy
   - Log user actions
   - Set up alerts for anomalies
"""


# ============================================================================
# DEPLOYMENT CONFIGURATIONS
# ============================================================================

"""
LOCAL DEPLOYMENT
   Command: streamlit run app.py
   Access: http://localhost:8501

STREAMLIT CLOUD DEPLOYMENT
   1. Push to GitHub
   2. Connect repository to Streamlit Cloud
   3. Configure secrets in .streamlit/secrets.toml
   4. Deploy with one click
   5. Access: https://yourapp.streamlit.app

DOCKER DEPLOYMENT
   Build: docker build -t traffic-dashboard .
   Run: docker run -p 8501:8501 traffic-dashboard

AWS/HEROKU/AZURE
   - Containerize with Docker
   - Push to container registry
   - Deploy using platform's CLI tools
   - Configure environment variables
"""


# ============================================================================
# TROUBLESHOOTING CONFIGURATIONS
# ============================================================================

"""
SLOW PERFORMANCE
   Solution: utils/plot_utils.py
   - Reduce sample_size in plot functions
   - Decrease histogram bins (nbinsx=30 → 20)
   - Use lower resolution for images

HIGH MEMORY USAGE
   Solution: prepare_test_data.py
   - Reduce number of samples: n_samples=200 → 100
   - Drop unnecessary features
   - Use data type optimization

MISSING DEPENDENCIES
   Solution: app.py
   - Comments can guide imports: "import streamlit as st"
   - Install requirements: pip install -r requirements.txt

PORT CONFLICTS
   Solution: Command line
   - Use different port: streamlit run app.py --server.port 8502
   - Kill process on port: lsof -ti:8501 | xargs kill -9
"""


# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

"""
Create .streamlit/config.toml for deployment:

[client]
showErrorDetails = false
maxMessageSize = 200

[logger]
level = "error"

[server]
port = 8501
headless = true
runOnSave = true
"""


# ============================================================================
# FEATURE CONFIGURATIONS
# ============================================================================

"""
FEATURE IMPORTANCE
   - Linear Regression: Uses absolute coefficient values
   - Tree Models: Uses model.feature_importances_ attribute
   - Custom: Implement in get_feature_importance() function

PREDICTION CONFIDENCE
   - Based on R² score in train metrics
   - Formula: confidence = max(0, r2_score * 100)
   - Range: 0-100%

RESIDUAL ANALYSIS
   - Calculated as: residuals = actual - predicted
   - Normal distribution indicates good model
   - Patterns suggest systematic errors

ERROR DISTRIBUTION
   - Histogram shows residual frequency
   - Bell curve is ideal
   - Skewed distribution indicates bias
"""


# ============================================================================
# ADVANCED CONFIGURATIONS
# ============================================================================

"""
MULTI-MODEL ENSEMBLING
   - Load predictions from multiple models
   - Calculate weighted average
   - Reduce prediction uncertainty

REAL-TIME UPDATES
   - Integrate live data source
   - Automatic model retraining schedule
   - Dashboard auto-refresh interval

CUSTOM METRICS
   - Implement in metrics_utils.py
   - Register in calculate_metrics()
   - Display in main app.py

FEATURE ENGINEERING
   - Modify data_utils.py load_test_data()
   - Add feature scaling/normalization
   - Create interaction terms
"""


# ============================================================================
# BEST PRACTICES
# ============================================================================

"""
✓ DO:
  - Keep utils modular and reusable
  - Document all changes with comments
  - Test changes locally before deployment
  - Use type hints in functions
  - Cache expensive operations
  - Validate user inputs
  - Log errors and predictions

✗ DON'T:
  - Hardcode file paths
  - Mix business logic with UI code
  - Store secrets in code
  - Make functions too long
  - Ignore error handling
  - Skip documentation
  - Use global variables
"""


# ============================================================================
# SUPPORT
# ============================================================================

"""
For detailed information:
- README.md: Comprehensive documentation
- QUICKSTART.md: Get started quickly
- validate_dashboard.py: Check installation
- Each .py file: Detailed docstrings

To validate configuration:
   python validate_dashboard.py
"""
