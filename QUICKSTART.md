# Traffic Volume Prediction Dashboard - Quick Start Guide

## 🚀 Installation (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs all required packages:
- **streamlit** - Interactive dashboard
- **pandas** - Data processing
- **scikit-learn** - ML models
- **plotly** - Interactive visualizations
- **numpy, joblib, matplotlib, seaborn** - Supporting libraries

### Step 2: (Optional) Generate Test Data
```bash
python prepare_test_data.py
```

Creates `test_data.csv` from your training data. If skipped, synthetic test data is generated automatically.

### Step 3: Launch the Dashboard
```bash
streamlit run app.py
```

The dashboard opens at: `http://localhost:8501`

---

## 📊 Dashboard Sections

### 1. **Sidebar Navigation** (Left Panel)
- 🎯 **Model Selection**: Choose from Linear Regression, Decision Tree, or Random Forest
- 📋 **Section Toggles**: Show/hide dashboard sections as needed
- ℹ️ **Model Info**: Display selected model details

### 2. **Model Evaluation Metrics** (Top)
Four key performance indicators:
- **MSE**: Mean Squared Error (lower is better)
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error (lower is better)
- **R² Score**: Goodness of fit (higher is better)

### 3. **Visualization Panel** (5 Tabs)
- **Actual vs Predicted Line**: Sequential comparison
- **Scatter Plot**: Accuracy distribution
- **Residual Plot**: Error analysis
- **Error Distribution**: Histogram of residuals
- **Performance Comparison**: Multi-model bar charts

### 4. **Model Comparison** (Table + Cards)
- Side-by-side metrics for all models
- Best MSE, MAE, R² Score highlights
- Comprehensive performance table

### 5. **Prediction Interface** (Make Predictions)
- Interactive sliders for 20+ features
- Real-time prediction
- Confidence metrics
- Prediction characteristics

### 6. **Data Insights** (3 Tabs)
- **Feature Importance**: Ranked feature influence
- **Feature Statistics**: Min, max, mean, std dev
- **Target Analysis**: Traffic volume distribution

---

## 🎮 How to Use

### Evaluating a Model
1. Open dashboard at `http://localhost:8501`
2. Select model from sidebar dropdown
3. View metrics in "Model Evaluation Metrics" section
4. Explore visualizations in tabs
5. Check "Data Insights" for feature patterns

### Making Predictions
1. Go to "Make Predictions" section
2. Adjust feature sliders to desired values
3. Click "🔮 Predict Traffic Volume" button
4. View prediction with confidence score
5. See prediction characteristics

### Comparing Models
1. Click "🔄 Model Comparison" in sidebar
2. View metrics table and best performer highlights
3. Switch to "Performance Comparison" tab
4. Analyze bar charts for MSE and R² Score

---

## 📁 Project Files

```
Your Project Root/
├── app.py                    ← Main dashboard application
├── requirements.txt          ← Install with: pip install -r requirements.txt
├── QUICKSTART.py             ← This guide as Python script
├── README.md                 ← Detailed documentation
├── validate_dashboard.py     ← Check installation status
├── prepare_test_data.py      ← Generate test data
├── datafile.csv              ← Training dataset
├── test_data.csv             ← Test dataset (generated)
│
├── Linear Regression.pkl     ← Trained model
├── Decision Tree.pkl         ← Trained model
├── Random Forest.pkl         ← Trained model
│
└── utils/                    ← Utility modules
    ├── __init__.py
    ├── model_utils.py        ← Model loading & caching
    ├── metrics_utils.py      ← Metrics calculation
    ├── plot_utils.py         ← Visualization functions
    └── data_utils.py         ← Data processing
```

---

## ⚡ Common Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Validate installation
python validate_dashboard.py

# Generate test data
python prepare_test_data.py

# Run dashboard
streamlit run app.py

# Run on specific port (if 8501 is in use)
streamlit run app.py --server.port 8502

# Run in development mode
streamlit run app.py --logger.level=debug
```

---

## 🔧 Customization Examples

### Change Dashboard Title
Edit `app.py`, line ~95:
```python
st.markdown("""
<h1>Your Custom Title Here</h1>
""", unsafe_allow_html=True)
```

### Modify Model List
Edit `app.py`, line ~235:
```python
model_names = ['Your Custom Model List']
```

### Adjust Colors
Edit `utils/plot_utils.py`, modify marker colors in visualization functions:
```python
marker=dict(color='rgba(YOUR, RGB, VALUES, 0.7)')
```

### Change Feature Sliders
Edit `app.py`, line ~470, modify range and steps:
```python
st.slider(feature, min_value=YOUR_MIN, max_value=YOUR_MAX, step=YOUR_STEP)
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "FileNotFoundError: test_data.csv"
```bash
python prepare_test_data.py
# OR dashboard auto-generates synthetic data
```

### "Models not found"
- Verify `.pkl` files are in project root
- Check exact file names match those in `app.py`

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### Slow dashboard
- Reduce test data size
- Close other applications
- Use: `streamlit run app.py --client.maxMessageSize=200`

---

## 📊 Dashboard Features Summary

| Feature | Purpose | Location |
|---------|---------|----------|
| Model Selection | Choose model to evaluate | Sidebar |
| Metrics Display | View MSE, MAE, R², RMSE | Top section |
| Visualizations | 5 interactive plot types | Main panel |
| Predictions | Generate new predictions | Bottom section |
| Feature Analysis | Importance and statistics | Expandable tabs |
| Model Comparison | Side-by-side metrics | Main panel |
| Error Analysis | Detailed error statistics | Expandable box |

---

## 🎯 Use Cases

1. **Model Selection**: Compare algorithms to find best performer
2. **Error Analysis**: Identify where models struggle
3. **Prediction**: Generate traffic volume forecasts
4. **Understanding**: Explore feature importance
5. **Portfolio**: Showcase ML skills with production dashboard
6. **Business**: Predict traffic for planning and optimization

---

## 💡 Pro Tips

- **Bookmark visualizations**: Use Plotly's camera icon to save chart images
- **Toggle sections**: Use sidebar checkboxes to focus on specific areas
- **Hover for details**: All charts show detailed info on hover
- **Download data**: All tables support download functionality
- **Share dashboard**: Deploy to Streamlit Cloud for web access

---

## 🚀 Next Steps After Setup

1. ✅ Install requirements: `pip install -r requirements.txt`
2. ✅ Launch dashboard: `streamlit run app.py`
3. ✅ Explore model performance
4. ✅ Generate predictions
5. ✅ Customize dashboard for your needs
6. ✅ Deploy to Streamlit Cloud (optional)

---

## 📞 Support

- **Documentation**: See README.md for detailed information
- **Validation**: Run `python validate_dashboard.py` to check setup
- **Code Quality**: Open `app.py` and `utils/*.py` for clean, documented code

---

**Ready? Run:** `streamlit run app.py` 🚀
