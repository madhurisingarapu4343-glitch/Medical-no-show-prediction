# 🏥 Medical Appointment No-Show Prediction

## 📌 Project Overview
This project predicts whether a patient will attend a scheduled medical appointment or not using Machine Learning. 

Missed appointments (no-shows) can cause major inefficiencies in hospitals. This system helps identify high-risk patients in advance so that necessary actions (like reminders) can be taken.

---

## 🚀 Features
- Data Cleaning & Preprocessing
- Feature Engineering (age groups, weekend, weather conditions, etc.)
- Handling Missing Values
- Class Imbalance Handling
- Machine Learning Models:
  - Random Forest
  - XGBoost (Final Model)
- Model Evaluation (Precision, Recall, F1-score, ROC-AUC)
- Time Series Forecasting (Daily Appointments)
- Streamlit Web App for Real-Time Prediction

---

## 🧠 Problem Statement
Predict whether a patient will **show up** or **not show up** for a medical appointment.

Target Variable:
- `no_show` (0 = Show, 1 = No Show)

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Statsmodels (ARIMA)
- Streamlit

---

## 📊 Model Performance

| Metric        | Score |
|--------------|------|
| Accuracy     | ~68% |
| Recall (No-show) | ~74% |
| ROC-AUC      | ~0.75 |

> Focus was on improving **recall** to correctly identify no-show patients.

---

## 📈 Time Series Forecasting
Used time series techniques to forecast daily appointment counts based on historical data.

---

## 💻 How to Run the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
