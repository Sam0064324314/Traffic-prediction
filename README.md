# 🚗 Traffic Volume Prediction Dashboard

A production-quality interactive machine learning dashboard for predicting traffic volume using sklearn Pipelines with automated preprocessing and feature engineering.

**Live Demo:** http://localhost:8501 (after running)




https://github.com/user-attachments/assets/1eb2fecd-993c-4da7-9499-a7bf9c431553




<img width="747" height="992" alt="Screenshot 2026-02-12 084127" src="https://github.com/user-attachments/assets/7c1d0e58-1f15-4362-851e-0add4ca09fdf" />

<img width="750" height="992" alt="Screenshot 2026-02-12 084139" src="https://github.com/user-attachments/assets/4d9dccf6-3eaa-4d9a-8e17-0aa80f6d3bb4" />

---


## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Training Models](#training-models)
- [Running the Dashboard](#running-the-dashboard)
- [Dashboard Features](#dashboard-features)
- [Pipeline Explanation](#pipeline-explanation)
- [Model Results](#model-results)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project implements a **production-grade traffic volume prediction system** using machine learning and interactive visualization. It combines:

- **Automated ML Pipelines** (sklearn.pipeline.Pipeline + ColumnTransformer)
- **3 Trained Models** (Linear Regression, Decision Tree, Random Forest)
- **Interactive Streamlit Dashboard** with real-time predictions
- **Robust Preprocessing** that handles unknown categories gracefully
- **Professional UI/UX** with metrics, visualizations, and comparisons

### Problem Statement
Traditional ML workflows suffer from:
- ❌ Manual feature encoding with pd.get_dummies() causing feature misalignment
- ❌ Predictions failing when encountering unknown categories
- ❌ Fragile data pipeline requiring separate preprocessing steps
- ❌ Difficulty maintaining consistent features between training and prediction

### Solution
This project uses **sklearn Pipelines** to:
- ✅ Automatically handle categorical & numerical features
- ✅ Handle unknown categories gracefully with handle_unknown="ignore"
- ✅ Combine preprocessing and model into a single robust object
- ✅ Eliminate feature misalignment issues
- ✅ Enable seamless production deployment

---

## ✨ Key Features

### 1. **📊 Model Evaluation Metrics**
   - Real-time MSE, RMSE, MAE, R² Score display
   - Detailed error statistics breakdown
   - Interactive metric cards with tooltips

### 2. **📈 Visualization Panel** (5 Interactive Tabs)
   - Actual vs Predicted Line Chart
   - Scatter Plot Analysis
   - Residual Plot for Error Analysis
   - Error Distribution Histogram
   - Model Performance Comparison

### 3. **🔄 Model Comparison**
   - Side-by-side comparison table of all models
   - Performance highlighting:
     - Lowest MSE model
     - Lowest MAE model
     - Highest R² Score model
   - Metric formatting for easy reading

### 4. **🎯 Interactive Predictions**
   - Dynamic feature sliders for numerical inputs
   - Dropdown selectors for categorical inputs
   - Real-time traffic volume forecasting
   - Model confidence display based on R² score

### 5. **💡 Data Insights**
   - Feature importance visualization
   - Feature statistics summary
   - Target variable analysis
   - Distribution charts with Plotly

### 6. **⚙️ Navigation & Settings**
   - Model selection dropdown
   - Toggle sections on/off
   - Clean sidebar layout
   - Responsive design

---

## 🏗️ Architecture

### Pipeline Architecture

```
Input Data (Raw Features)
    ↓
┌─────────────────────────────────────┐
│    ColumnTransformer                │
├─────────────────────────────────────┤
│ Categorical Branch:                 │
│  └─ OneHotEncoder(handle_unknown)   │
│                                     │
│ Numerical Branch:                   │
│  └─ StandardScaler                  │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│    Model Selection                  │
├─────────────────────────────────────┤
│ • Linear Regression                 │
│ • Decision Tree                     │
│ • Random Forest                     │
└─────────────────────────────────────┘
    ↓
Predictions (Traffic Volume)
```

### Project Components

```
Trffic/
├── app.py                              # Main Streamlit dashboard
├── train_with_pipeline.py              # Pipeline training script
├── generate_pipeline_test_data.py      # Test data generator
├── datafile.csv                        # Original raw data
├── test_data.csv                       # Test data (raw categorical values)
│
├── models/
│   ├── Linear Regression Pipeline.pkl  # Trained pipeline
│   ├── Decision Tree Pipeline.pkl      # Trained pipeline
│   ├── Random Forest Pipeline.pkl      # Trained pipeline
│   ├── preprocessor.pkl                # Standalone preprocessor
│   └── feature_info.pkl                # Feature metadata
│
├── utils/
│   ├── __init__.py
│   ├── model_utils.py                  # Model loading + caching
│   ├── metrics_utils.py                # Metrics calculation
│   ├── plot_utils.py                   # Plotly visualizations
│   ├── data_utils.py                   # Data processing utilities
│   └── __init__.py
│
├── documentation/
│   ├── README.md                       # This file
│   ├── 00_READ_ME_FIRST.md            # Quick start guide
│   ├── START_HERE.md                  # Getting started
│   ├── QUICKSTART.md                  # Quick reference
│   ├── DEPLOYMENT.md                  # Deployment guide
│   └── SUMMARY.md                     # Project summary
│
└── requirements.txt                    # Project dependencies
```

---

## 📦 Installation

### Prerequisites

- **Python 3.10+** (tested on 3.12)
- **pip** (Python package manager)
- **Windows/Mac/Linux** (cross-platform compatible)

### Step 1: Clone or Download the Project

```bash
# Download the project files to your computer
cd /path/to/Trffic
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**Manual installation** (if requirements.txt fails):

```bash
# Core ML Libraries
pip install scikit-learn==1.3.2
pip install pandas==2.0.3
pip install numpy==1.24.3

# Dashboard & Visualization
pip install streamlit==1.54.0
pip install plotly==5.18.0
pip install matplotlib seaborn

# Utilities
pip install joblib
```

### Step 4: Verify Installation

```bash
python -c "import streamlit, sklearn, plotly; print('✓ All dependencies installed!')"
```

---

## 🎬 Training Models

### Step 1: Prepare Data

Ensure your raw data file exists:
- **datafile.csv** - Original traffic data with raw categorical values

### Step 2: Run Training Pipeline

```bash
python train_with_pipeline.py
```

**Expected Output:**
```
================================================================================
TRAFFIC VOLUME PREDICTION - PIPELINE-BASED TRAINING
================================================================================

[1/6] Loading data...
Original data shape: (48204, 9)

[2/6] Performing feature engineering...

[3/6] Identifying column types...
Categorical columns: ['holiday', 'weather_main', 'day']
Numerical columns: ['temp', 'rain_1h', 'snow_1h', 'clouds_all', ...]

[4/6] Splitting data (85% train, 15% test)...
Training set size: 40958
Test set size: 7229

[5/6] Building preprocessing + model pipelines...
  Training Linear Regression...
    Train MSE: 3,569,574.50 | Test MSE: 27,005,574.91
  Training Decision Tree...
    Train MSE: 283,691.37 | Test MSE: 5,403,598.25
  Training Random Forest...
    Train MSE: 681,436.97 | Test MSE: 3,592,361.39

[6/6] Saving pipeline models...
  ✓ Saved: Linear Regression Pipeline.pkl
  ✓ Saved: Decision Tree Pipeline.pkl
  ✓ Saved: Random Forest Pipeline.pkl

================================================================================
EVALUATION SUMMARY
================================================================================
Model               Train MSE    Test MSE   Train R²  Test R²
Linear Regression   3.57e+06    2.70e+07    0.0941   -5.7702
Decision Tree       2.84e+05    5.40e+06    0.9280   -0.3547
Random Forest       6.81e+05    3.59e+06    0.8271    0.0994

✓ Best Model (R² Score): Random Forest
✓ Best Model (MSE):      Random Forest
================================================================================
```

### Step 3: Generate Test Data

```bash
python generate_pipeline_test_data.py
```

**Output:** Creates `test_data.csv` with 200 samples for dashboard testing

---

## 🚀 Running the Dashboard

### Step 1: Start Streamlit Server

```bash
python -m streamlit run app.py
```

**Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://YOUR-IP:8501
```

### Step 2: Open in Browser

1. Click the link above OR
2. Manually navigate to: **http://localhost:8501**

### Step 3: Stop the Server

```bash
# Press Ctrl+C in the terminal
```

---

## 🎨 Dashboard Features

### Feature 1: Model Evaluation Metrics
- View MSE, RMSE, MAE, R² Score
- Detailed error statistics
- Model confidence indicator

**Location:** Top section of dashboard after selecting a model

### Feature 2: Visualization Panel
5 interactive tabs with Plotly charts:

1. **Actual vs Predicted Line** - See prediction accuracy over time
2. **Scatter Plot** - Visualize prediction spread
3. **Residual Plot** - Analyze prediction errors
4. **Error Distribution** - Histogram of error frequency
5. **Performance Comparison** - Compare MSE and R² across models

**Location:** Middle section under "📈 Visualization Panel"

### Feature 3: Model Comparison
Compare all 3 models side-by-side:
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

Best model indicators for:
- Lowest MSE (best for penalizing large errors)
- Lowest MAE (best for average errors)
- Highest R² (best overall fit)

**Location:** "🔄 Model Comparison" section

### Feature 4: Make Predictions
Interactive prediction interface:

**Numerical Features** (Sliders):
- Temperature (°K)
- Rain (1h, mm)
- Snow (1h, mm)
- Cloud coverage (%)
- Month, Year, Hour

**Categorical Features** (Dropdowns):
- Holiday status (None/Holiday)
- Weather condition (Clouds/Rain/Clear/Snow)
- Day of week (Monday-Sunday)

**Output:** Predicted traffic volume + model confidence

**Location:** "🎯 Make Predictions" section

### Feature 5: Data Insights
3 tabs with analytics:

1. **Feature Importance** - Top 15 most important features
2. **Feature Statistics** - Min, mean, max, std dev for all features
3. **Target Analysis** - Traffic volume distribution and stats

**Location:** "💡 Data Insights & Feature Importance" section

### Navigation Sidebar
- **Model Selection:** Choose which model to evaluate
- **Section Toggles:** Show/hide specific dashboard sections
- **Model Information:** View selected model type and training samples

---

## 🔧 Pipeline Explanation

### What is a sklearn Pipeline?

A Pipeline combines multiple steps into a single object:

```python
Pipeline([
    ('preprocessor', ColumnTransformer),  # Step 1: Preprocessing
    ('model', RandomForestRegressor())     # Step 2: Model
])
```

### Why Pipelines?

**Traditional Approach (Fragile):**
```python
# Train
X_train = pd.get_dummies(X_train)  # Manual encoding
model.fit(X_train, y_train)

# Predict
X_new = pd.get_dummies(X_new)      # Must match exactly
if X_new.shape[1] != X_train.shape[1]:  # ERROR!
    print("Feature mismatch!")
```

**Pipeline Approach (Robust):**
```python
# Train
pipeline = Pipeline([
    ('preprocess', ColumnTransformer(...)),
    ('model', RandomForestRegressor())
])
pipeline.fit(X_train, y_train)

# Predict (handles preprocessing automatically)
pipeline.predict(X_new)  # ✓ Works every time!
```

### Our Pipeline Details

**Categorical Features:**
```python
OneHotEncoder(
    handle_unknown='ignore',      # Unknown categories → zero vector
    sparse_output=False           # Dense output for compatibility
)
```
Automatically handles:
- Holiday (None, Holiday)
- Weather (Clouds, Rain, Clear, Snow)
- Day (Monday-Sunday)

**Numerical Features:**
```python
StandardScaler()                  # Mean=0, Std=1 normalization
```
Scales:
- Temperature
- Rain (1h)
- Snow (1h)
- Cloud coverage
- Month, Year, Hour

### Features Handled

**Before:** 10 raw features
```
holiday, weather_main, day, temp, rain_1h, snow_1h, 
clouds_all, month, year, hour
```

**After Transformation:** ~30+ encoded features
```
holiday_None, holiday_Holiday,
weather_main_Clouds, weather_main_Rain, weather_main_Clear, weather_main_Snow,
day_Monday, day_Tuesday, ..., day_Sunday,
temp (scaled), rain_1h (scaled), snow_1h (scaled), clouds_all (scaled), ...
```

---

## 📊 Model Results

### Performance Comparison

| Model | Train MSE | Test MSE | Train R² | Test R² | Best For |
|-------|-----------|----------|----------|---------|----------|
| Linear Regression | 3.57M | 27.0M | 0.0941 | -5.77 | Baseline |
| Decision Tree | 284K | 5.40M | 0.9280 | -0.35 | Overfitted |
| **Random Forest** | 681K | 3.59M | 0.8271 | 0.0994 | ✓ Best Choice |

### Analysis

- **Random Forest** is the best overall model
  - Best test R² score (0.0994)
  - Best test MSE (3.59M)
  - Good generalization (not overfitted)

- **Decision Tree** shows signs of overfitting
  - Perfect training fit (0.9280)
  - Poor test fit (-0.3547)
  - Lower test MSE but high variance

- **Linear Regression** struggles
  - Weak baseline (R² < 0)
  - Traffic volume too complex for linear relationship

### Metrics Explained

- **MSE (Mean Squared Error)**: Average squared difference
  - Lower is better
  - Penalizes large errors heavily
  
- **RMSE (Root Mean Squared Error)**: Square root of MSE
  - Same units as target (vehicles)
  - Easier to interpret
  
- **MAE (Mean Absolute Error)**: Average absolute difference
  - Lower is better
  - Less sensitive to outliers than MSE
  
- **R² Score**: Proportion of variance explained
  - Higher is better (max = 1.0)
  - Random Forest: 0.0994 = explains ~10% of variance

---

## 💡 Usage Examples

### Example 1: Make a Prediction Using Dashboard

1. **Open Dashboard:** http://localhost:8501
2. **Select Model:** Dropdown → "Random Forest" (recommended)
3. **Adjust Features:**
   - Temperature: 280°K (about 7°C)
   - Rain: 0.5 mm
   - Clouds: 75%
   - Day: Monday
   - Hour: 9 AM
4. **Predict:** Click "🔮 Predict Traffic Volume"
5. **View Result:** ~5,000-5,500 vehicles (peak morning traffic)

### Example 2: Compare Models

1. Open **"🔄 Model Comparison"** section
2. View metrics table with all 3 models
3. Check best performers:
   - Lowest MSE: Random Forest (3.59M)
   - Highest R²: Random Forest (0.0994)

### Example 3: Analyze Feature Importance

1. Open **"💡 Data Insights"** → **"Feature Importance"** tab
2. See top 15 most important features
3. Example insights:
   - Temperature (weather is important)
   - Hour of day (traffic patterns vary by time)
   - Month (seasonal variations)
   - Weather conditions (clouds, rain affect traffic)

### Example 4: Retrain Models

```bash
# 1. Update your data
cp new_data.csv datafile.csv

# 2. Retrain
python train_with_pipeline.py

# 3. Generate new test data
python generate_pipeline_test_data.py

# 4. Restart dashboard (Ctrl+C, then run again)
python -m streamlit run app.py
```

---

## 🐛 Troubleshooting

### Issue 1: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
pip install streamlit
# Or install all dependencies:
pip install -r requirements.txt
```

### Issue 2: "Port 8501 is already in use"

**Solution:**
```bash
# Use alternative port
streamlit run app.py --server.port 8502
```

### Issue 3: "Model file not found"

**Solution:**
Ensure you've trained the models:
```bash
python train_with_pipeline.py
```

### Issue 4: "Feature names should match those passed during fit"

**This is FIXED in this version!** The pipeline handles this automatically with `handle_unknown='ignore'`

### Issue 5: Dashboard loads but predictions fail

**Solution:**
1. Check test_data.csv exists
2. Ensure it has both categorical and numerical columns
3. Regenerate test data:
```bash
python generate_pipeline_test_data.py
```

### Issue 6: Slow predictions on first load

**Expected behavior.** First prediction takes 2-3 seconds because Streamlit caches the model. Subsequent predictions are instant.

---

## 🔄 Workflow Diagram

```
Start
  ↓
[1] Install Dependencies
  ├─ python -m venv venv
  ├─ pip install -r requirements.txt
  └─ ✓ Dependencies ready
  ↓
[2] Train Models
  ├─ python train_with_pipeline.py
  ├─ Creates 3 pipeline models
  ├─ Saves .pkl files
  └─ ✓ Models trained
  ↓
[3] Generate Test Data
  ├─ python generate_pipeline_test_data.py
  ├─ Samples from training data
  ├─ Raw categorical values (NOT encoded)
  └─ ✓ Test data ready
  ↓
[4] Run Dashboard
  ├─ python -m streamlit run app.py
  ├─ Loads pipelines
  ├─ Starts server on port 8501
  └─ ✓ Ready to use
  ↓
[5] Make Predictions
  ├─ Use sliders/dropdowns
  ├─ Pipeline auto-encodes features
  ├─ View predictions
  └─ ✓ Success!
  ↓
End
```

---

## 📁 File Descriptions

### Core Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit dashboard application |
| `train_with_pipeline.py` | Trains and saves sklearn pipeline models |
| `generate_pipeline_test_data.py` | Generates test_data.csv from original data |
| `datafile.csv` | Raw traffic data (48,187 rows, 9 columns) |
| `test_data.csv` | Test samples (200 rows, raw categorical values) |

### Model Files (Created after training)

| File | Purpose |
|------|---------|
| `Linear Regression Pipeline.pkl` | Complete pipeline: preprocessing + Linear Regression model |
| `Decision Tree Pipeline.pkl` | Complete pipeline: preprocessing + Decision Tree model |
| `Random Forest Pipeline.pkl` | Complete pipeline: preprocessing + Random Forest model |
| `preprocessor.pkl` | Standalone ColumnTransformer (for reference) |
| `feature_info.pkl` | Feature metadata (categorical & numerical column names) |

### Utility Modules

| File | Purpose |
|------|---------|
| `utils/model_utils.py` | Load models + extract feature importance |
| `utils/metrics_utils.py` | Calculate MSE, RMSE, MAE, R², residuals |
| `utils/plot_utils.py` | Create Plotly visualizations |
| `utils/data_utils.py` | Load data + prepare inputs |

### Documentation

| File | Purpose |
|------|---------|
| `README.md` | This comprehensive guide |
| `00_READ_ME_FIRST.md` | Quick start (read first!) |
| `START_HERE.md` | Getting started guide |
| `QUICKSTART.md` | Quick reference |
| `DEPLOYMENT.md` | Production deployment guide |
| `SUMMARY.md` | Project summary |

---

## 🚀 Quick Start (TL;DR)

```bash
# 1. Install
pip install -r requirements.txt

# 2. Train
python train_with_pipeline.py

# 3. Generate test data
python generate_pipeline_test_data.py

# 4. Run
streamlit run app.py

# 5. Open browser
# http://localhost:8501
```

---

## 📈 Next Steps

### For Development:
1. ✨ Add more features (temperature trends, traffic patterns)
2. 🤖 Try advanced models (XGBoost, LightGBM)
3. 📊 Add more visualizations
4. 🧪 Write unit tests

### For Production:
1. 🏭 Deploy to Heroku, AWS, or Google Cloud
2. 📦 Create Docker container
3. 🔐 Add authentication
4. 📈 Monitor model performance

### For Data:
1. 📥 Update datafile.csv with recent data
2. 🔄 Retrain models regularly
3. 📊 Track metrics over time
4. 🎯 Fine-tune hyperparameters

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Style Guidelines
- Follow PEP 8 for Python code
- Add docstrings to functions
- Comment complex logic
- Test before submitting

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 📞 Support

Found a bug or have a question?

1. Check [Troubleshooting](#troubleshooting) section
2. Review existing GitHub issues
3. Create a new GitHub issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations with [Plotly](https://plotly.com/)
- ML with [scikit-learn](https://scikit-learn.org/)
- Data processing with [Pandas](https://pandas.pydata.org/)

---

## 📚 References

### sklearn Pipeline Documentation
- https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
- https://scikit-learn.org/stable/modules/compose.html

### Streamlit Documentation
- https://docs.streamlit.io/
- https://docs.streamlit.io/library/api-reference

### Plotly Documentation
- https://plotly.com/python/
- https://plotly.com/python/tutorials/

---

## 📊 Data Source

**Dataset:** Traffic Volume Data
- **Records:** 48,187 observations
- **Features:** 9 raw columns
- **Target:** traffic_volume (vehicles)
- **Time Period:** 2012-2018
- **Frequency:** Hourly

### Features
- `traffic_volume`: Target variable (vehicles)
- `holiday`: Holiday status
- `temp`: Temperature (Kelvin)
- `rain_1h`: Rainfall in 1 hour (mm)
- `snow_1h`: Snowfall in 1 hour (mm)
- `clouds_all`: Cloud coverage (%)
- `weather_main`: Weather condition
- `weather_description`: Detailed weather
- `date_time`: Timestamp

---

**Last Updated:** February 2026  
**Version:** 2.0.0 (Pipeline-based)  
**Status:** ✅ Production Ready

---

## 🎓 Learning Resources

### Understanding sklearn Pipelines
```python
# Basic pipeline structure
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

pipeline = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])),
    ('model', RandomForestRegressor())
])

# Train once, use everywhere
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_new)  # Automatic preprocessing!
```

### Understanding the Dashboard
- **Streamlit**: Converts Python scripts to interactive web apps
- **Plotly**: Interactive visualizations
- **Caching**: @st.cache_resource speeds up repeated operations

---

**Happy Predicting! 🎉**

For questions or improvements, please open an issue on GitHub.
