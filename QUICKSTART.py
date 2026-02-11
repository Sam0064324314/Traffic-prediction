#!/usr/bin/env python
"""
Quick Start Guide for Traffic Volume Prediction Dashboard

This script provides step-by-step instructions to get the dashboard running.
"""

import subprocess
import sys
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def print_step(step_num, text):
    """Print a formatted step."""
    print(f"Step {step_num}: {text}")
    print("-" * 70)


def main():
    print_header("🚗 Traffic Volume Prediction Dashboard - Quick Start")
    
    print("This dashboard provides:")
    print("  ✓ Interactive model selection and evaluation")
    print("  ✓ Comprehensive performance visualizations")
    print("  ✓ Real-time traffic volume predictions")
    print("  ✓ Feature importance analysis")
    print("  ✓ Model comparison across 3 algorithms")
    
    print_step(1, "Install Required Dependencies")
    print("Run this command to install all required packages:\n")
    print("   pip install -r requirements.txt\n")
    print("This will install:")
    print("   • streamlit       - Interactive dashboard framework")
    print("   • pandas          - Data processing")
    print("   • numpy           - Numerical computing")
    print("   • scikit-learn    - Machine learning models")
    print("   • plotly          - Interactive visualizations")
    print("   • joblib          - Model loading")
    print("   • matplotlib      - Plotting library")
    print("   • seaborn         - Statistical visualizations")
    
    print_step(2, "Generate Test Data (Optional)")
    print("If you want to generate test data from the training dataset:\n")
    print("   python prepare_test_data.py\n")
    print("This creates test_data.csv for model evaluation.")
    print("If test_data.csv is missing, the dashboard will generate synthetic data.")
    
    print_step(3, "Launch the Dashboard")
    print("Run the dashboard with:\n")
    print("   streamlit run app.py\n")
    print("The dashboard will open in your browser at:")
    print("   http://localhost:8501")
    
    print_step(4, "Using the Dashboard")
    print("""
Key Features:

📊 Model Evaluation
   - Select a model from the sidebar
   - View MSE, RMSE, MAE, R² Score metrics
   - Expand detailed error statistics

📈 Visualizations
   - 5 interactive plot types
   - Actual vs Predicted comparison
   - Residual analysis
   - Error distribution

🔄 Model Comparison
   - Side-by-side metrics table
   - Best performer highlights
   - Performance rankings

🎯 Predictions
   - Interactive sliders for features
   - One-click predictions
   - Confidence metrics

💡 Data Insights
   - Feature importance rankings
   - Feature statistics
   - Target variable analysis
    """)
    
    print_step(5, "File Structure")
    print("""
Project Directory:
├── app.py                           (Main application)
├── requirements.txt                 (Dependencies)
├── prepare_test_data.py            (Data generation)
├── validate_dashboard.py           (Validation script)
├── README.md                       (Full documentation)
├── datafile.csv                    (Training data)
├── test_data.csv                   (Test data)
├── Linear Regression.pkl           (Trained model)
├── Decision Tree.pkl               (Trained model)
├── Random Forest.pkl               (Trained model)
└── utils/
    ├── __init__.py
    ├── model_utils.py
    ├── metrics_utils.py
    ├── plot_utils.py
    └── data_utils.py
    """)
    
    print_step(6, "Troubleshooting")
    print("""
"Module not found" errors:
   → Run: pip install -r requirements.txt

Models not loading:
   → Check file names: Linear Regression.pkl, Decision Tree.pkl, Random Forest.pkl
   → Ensure files are in the project root directory

Port already in use:
   → Run: streamlit run app.py --logger.level=debug --server.port 8502

Memory issues:
   → Reduce test data size in prepare_test_data.py
   → Use: streamlit run app.py --client.maxMessageSize=200
    """)
    
    print_step(7, "Next Steps")
    print("""
1. Install dependencies:
   pip install -r requirements.txt

2. (Optional) Generate test data:
   python prepare_test_data.py

3. Launch the dashboard:
   streamlit run app.py

4. Open http://localhost:8501 in your browser

5. Explore the dashboard using the sidebar navigation
    """)
    
    print_header("✅ You're Ready to Go!")
    print("""
Your production-quality traffic volume prediction dashboard is ready.

The dashboard includes:
  ✓ Clean, professional UI/UX design
  ✓ Modular, reusable Python code
  ✓ Advanced visualizations with Plotly
  ✓ Model caching for performance
  ✓ Comprehensive error handling
  ✓ Full documentation and type hints

Start with: streamlit run app.py
    """)


if __name__ == "__main__":
    main()
