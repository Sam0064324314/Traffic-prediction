# Contributing to Traffic Volume Prediction Dashboard

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 How to Contribute

### 1. Report a Bug
If you find a bug, please create a GitHub Issue with:
- **Title**: Clear, concise description of the bug
- **Description**: Detailed explanation of the issue
- **Steps to Reproduce**: How to reproduce the bug
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: Python version, OS, installed packages

### 2. Suggest an Enhancement
Have an idea to improve the project? Open an Issue with:
- **Title**: Feature request or enhancement idea
- **Description**: Detailed explanation of the feature
- **Use Case**: Why this feature would be useful
- **Possible Implementation**: Any ideas on how to implement it

### 3. Submit a Pull Request (PR)

#### Step 1: Fork the Repository
```bash
# Click the "Fork" button on GitHub
```

#### Step 2: Clone Your Fork
```bash
git clone https://github.com/YOUR-USERNAME/traffic-volume-prediction.git
cd traffic-volume-prediction
```

#### Step 3: Create a Feature Branch
```bash
# Create a new branch for your feature
git checkout -b feature/your-feature-name
# Or for bug fixes:
git checkout -b bugfix/your-bug-fix-name
```

#### Step 4: Make Your Changes
```bash
# Edit files, add features, or fix bugs
# Ensure your code follows PEP 8 standards
```

#### Step 5: Test Your Changes
```bash
# Test locally before submitting
python -m streamlit run app.py
# Manually test all affected features
```

#### Step 6: Commit Your Changes
```bash
# Stage changes
git add .

# Commit with a clear message
git commit -m "Add feature: [clear description of changes]"
# Or for fixes:
git commit -m "Fix: [description of bug fix]"
```

#### Step 7: Push to Your Fork
```bash
git push origin feature/your-feature-name
```

#### Step 8: Create a Pull Request
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill in the PR template:
   - **Title**: Clear description
   - **Description**: Detailed explanation
   - **Related Issues**: Link to related issues (closes #123)
   - **Changes**: What was changed
   - **Testing**: How you tested the changes

---

## 📝 Code Style Guidelines

### Python Code
- Follow **PEP 8** style guide
- Use **4 spaces** for indentation (not tabs)
- Keep lines **under 100 characters**
- Use **meaningful variable names**

### Example
```python
# ❌ Bad
def predict(m,d):
    try:
        res = m.predict(d)
        return res
    except:
        pass

# ✅ Good
def predict(pipeline, input_data):
    """
    Make predictions using the trained pipeline.
    
    Args:
        pipeline: sklearn.pipeline.Pipeline object
        input_data: DataFrame with raw features
    
    Returns:
        numpy array of predictions
    """
    try:
        predictions = pipeline.predict(input_data)
        return predictions
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return None
```

### Docstrings
All functions should have docstrings:

```python
def calculate_metrics(y_true, y_pred):
    """
    Calculate model evaluation metrics.
    
    Args:
        y_true (array-like): Actual values
        y_pred (array-like): Predicted values
    
    Returns:
        dict: Dictionary containing MSE, MAE, RMSE, R² Score
    
    Example:
        >>> y_true = [3, -0.5, 2]
        >>> y_pred = [2.5, 0.0, 2]
        >>> metrics = calculate_metrics(y_true, y_pred)
        >>> print(metrics['MSE'])
    """
```

### Comments
- Use comments to explain **why**, not **what**
- Use comments sparingly
- Keep comments up-to-date with code

```python
# ❌ Bad - states the obvious
x = x + 1  # increment x

# ✅ Good - explains the logic
# Skip the first prediction as it's unreliable during model warm-up
predictions = predictions[1:]
```

---

## 🧪 Testing

### Before Submitting a PR
1. Test locally: `streamlit run app.py`
2. Test all dashboard sections
3. Test predictions with various inputs
4. Check for any errors in console
5. Verify no new dependencies broke anything

### For Model Changes
```bash
# Train new models
python train_with_pipeline.py

# Generate test data
python generate_pipeline_test_data.py

# Test dashboard loads with new models
python -m streamlit run app.py
```

---

## 📋 PR Review Process

### What We Look For
- ✅ Code follows style guidelines
- ✅ All tests pass
- ✅ PR has a clear description
- ✅ Changes are focused and not too large
- ✅ Docstrings and comments are clear
- ✅ No breaking changes to existing APIs

### Review Timeline
- Small PRs (< 100 lines): 1-2 days
- Medium PRs (100-500 lines): 2-5 days
- Large PRs (> 500 lines): 5+ days or may be asked to split

### Addressing Feedback
- Respond to all comments
- Make requested changes
- Push updates to your branch (no need to close and reopen)
- Re-request review after changes

---

## 🎯 Priority Areas for Contributions

### High Priority
- 🐛 Bug fixes (especially crashes or data loss)
- 📊 Improve model accuracy
- 🎨 UI/UX enhancements
- 📚 Documentation improvements

### Medium Priority
- ✨ Minor feature additions
- ⚡ Performance optimizations
- 🧪 Test coverage
- 📈 Visualization improvements

### Low Priority
- 💬 Code style tweaks
- 📝 Typo fixes
- 🎯 Minor refactoring

---

## 🚀 Becoming a Maintainer

Contributors who consistently provide high-quality contributions may be offered maintainer status, granting:
- Ability to merge PRs
- Ability to manage issues
- Ability to release new versions
- Responsibility for code quality

---

## 💬 Questions?

- **Questions about contributing**: Open a Discussion
- **Questions about the code**: Comment on the relevant PR/Issue
- **General questions**: Email or open an Issue

---

## 📖 Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [How to Write Good Commit Messages](https://chris.beams.io/posts/git-commit/)
- [sklearn Documentation](https://scikit-learn.org/stable/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## ❤️ Thank You!

We appreciate all contributions, no matter how small. Every contribution helps make this project better!

---

**Last Updated:** February 2026
