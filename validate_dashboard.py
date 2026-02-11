"""
Quick validation script to test if all imports work and basic functionality is operational.
"""

import sys
import os
from pathlib import Path

# Add project to path
project_root = r'c:\Users\jains\OneDrive\Desktop\Trffic'
sys.path.insert(0, project_root)
os.chdir(project_root)

print("=" * 60)
print("🔍 Dashboard Validation Report")
print("=" * 60)

# Test 1: Verify file structure
print("\n1️⃣  File Structure Check:")
required_files = [
    'app.py',
    'requirements.txt',
    'prepare_test_data.py',
    'README.md',
    'Linear Regression.pkl',
    'Decision Tree.pkl',
    'Random Forest.pkl'
]

required_dirs = ['utils']

all_good = True
for file in required_files:
    path = Path(project_root) / file
    exists = path.exists()
    status = "✓" if exists else "✗"
    print(f"   {status} {file}")
    if not exists:
        all_good = False

for dir_name in required_dirs:
    path = Path(project_root) / dir_name
    exists = path.exists() and path.is_dir()
    status = "✓" if exists else "✗"
    print(f"   {status} {dir_name}/")
    if not exists:
        all_good = False

# Test 2: Verify utils module
print("\n2️⃣  Utils Module Check:")
utils_files = [
    'utils/__init__.py',
    'utils/model_utils.py',
    'utils/metrics_utils.py',
    'utils/plot_utils.py',
    'utils/data_utils.py'
]

for file in utils_files:
    path = Path(project_root) / file
    exists = path.exists()
    status = "✓" if exists else "✗"
    print(f"   {status} {file}")
    if not exists:
        all_good = False

# Test 3: Import checks
print("\n3️⃣  Dependencies Check:")
dependencies = [
    ('pandas', 'Data processing'),
    ('numpy', 'Numerical computing'),
    ('sklearn', 'Machine Learning'),
    ('plotly', 'Interactive visualizations'),
    ('joblib', 'Model serialization'),
]

missing_deps = []
for package, description in dependencies:
    try:
        __import__(package)
        print(f"   ✓ {package:20} - {description}")
    except ImportError:
        print(f"   ✗ {package:20} - {description} [MISSING]")
        missing_deps.append(package)
        all_good = False

# Test 4: Utils imports
print("\n4️⃣  Utils Module Imports:")
try:
    from utils import (
        load_model,
        calculate_metrics,
        plot_actual_vs_predicted,
        get_feature_stats
    )
    print("   ✓ All utils imports successful")
except ImportError as e:
    print(f"   ✗ Utils import failed: {e}")
    all_good = False

# Test 5: Model loading
print("\n5️⃣  Model Files Check:")
model_files = [
    'Linear Regression.pkl',
    'Decision Tree.pkl',
    'Random Forest.pkl'
]

try:
    import joblib
    for model_file in model_files:
        try:
            model = joblib.load(model_file)
            print(f"   ✓ {model_file} - {type(model).__name__}")
        except Exception as e:
            print(f"   ✗ {model_file} - Failed to load: {str(e)[:40]}")
            all_good = False
except ImportError:
    print("   ✗ joblib not installed")
    all_good = False

# Test 6: Summary
print("\n" + "=" * 60)
if all_good:
    print("✅ All checks PASSED! Dashboard is ready to run.")
    print("\nTo start the dashboard, run:")
    print("   streamlit run app.py")
else:
    print("⚠️  Some checks FAILED. Please review the issues above.")
    if missing_deps:
        print(f"\nMissing packages: {', '.join(missing_deps)}")
        print("Install with: pip install -r requirements.txt")

print("=" * 60)
