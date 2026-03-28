 🏠 House Price Prediction using Machine Learning (XGBoost)

## 📌 Project Overview
This project predicts house prices using Machine Learning based on various house-related features such as area, bedrooms, bathrooms, floors, location, condition, and garage availability.

The model uses **XGBoost Regressor**, which provides high prediction accuracy and handles complex relationships in data.

---

## 📂 Dataset Information
The dataset contains **2000 records** and **14 columns**.

### Features Used
- `Id`
- `Area`
- `Bedrooms`
- `Bathrooms`
- `Floors`
- `YearBuilt`
- `Location`
- `Condition`
- `Garage`
- `Price` *(Target Variable)*
- `HouseAge`
- `PricePerSqFt`
- `HasGarage`
- `TotalRooms`

---

## 🔧 Added Modifications
The dataset was modified to improve the machine learning workflow.

### ✅ Missing Values Added
Missing values were intentionally introduced in:
- `Area`
- `Bathrooms`
- `Location`
- `Condition`

This helps in demonstrating **data preprocessing and missing value handling**.

### ✅ New Features Added
Additional features created:
- `HouseAge`
- `PricePerSqFt`
- `HasGarage`
- `TotalRooms`

---

## ⚙️ Workflow
1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis
4. Train-Test Split
5. Model Training using XGBoost
6. Model Evaluation
7. Deployment using Streamlit

---

## 🤖 Model Used
**XGBoost Regressor**

### Why XGBoost?
- High accuracy
- Handles missing values
- Reduces overfitting
- Boosting-based algorithm

---

## 📊 Evaluation Metrics
The model is evaluated using:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Square Error)
- R² Score

---

## 🚀 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Matplotlib

---

## ▶️ How to Run
Install dependencies:
```bash
pip install pandas numpy scikit-learn xgboost streamlit
```

Run the project:
```bash
python train_model.py
streamlit run app.py
```

---

## 📈 Future Improvements
- Add location encoding
- Hyperparameter tuning
- Online deployment
- Advanced feature engineering

---

## 👨‍💻 Author
Developed as a Machine Learning mini project for house price prediction.
