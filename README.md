# ❤️ Heart Disease Prediction Using Machine Learning

A Machine Learning project that predicts the likelihood of heart disease using patient health parameters. The project explores multiple classification algorithms and deploys an SVM-based prediction model through an interactive Streamlit web application.

## 🚀 Live Application

**Try the application:** [Heart Disease Prediction]((https://heart-disease-predictor-appuw62ycyak2wwxrnkikea.streamlit.app/))

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. This project uses machine learning classification techniques to analyze patient health information and predict whether a person is likely to have heart disease.

The project includes data exploration, preprocessing, feature encoding, feature scaling, model training, and evaluation.

## 🧠 Machine Learning Algorithms

Six classification algorithms were implemented and evaluated:

| Algorithm                    | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| Logistic Regression          | Linear classification model                      |
| Decision Tree                | Tree-based classification                        |
| K-Nearest Neighbors (KNN)    | Distance-based classification                    |
| Random Forest                | Ensemble learning algorithm                      |
| Support Vector Machine (SVM) | Classification using optimal decision boundaries |
| Gaussian Naive Bayes         | Probabilistic classification                     |

**Final selected model:** Support Vector Machine (SVM)

## 📊 Dataset

The project uses a heart disease dataset containing patient health information.

### Features Used

| Feature        | Description             |
| -------------- | ----------------------- |
| Age            | Patient's age           |
| Sex            | Gender                  |
| ChestPainType  | Type of chest pain      |
| RestingBP      | Resting blood pressure  |
| Cholesterol    | Serum cholesterol       |
| FastingBS      | Fasting blood sugar     |
| MaxHR          | Maximum heart rate      |
| ExerciseAngina | Exercise-induced angina |
| Oldpeak        | ST depression           |
| ST_Slope       | Slope of the ST segment |

**Target Variable:** `HeartDisease`

- `0` = No heart disease
- `1` = Heart disease

Note: RestingECG was excluded during model training.

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

## 🔬 Project Workflow

1. **Data Loading:** Import the heart disease dataset using Pandas.
2. **Exploratory Data Analysis:** Examine dataset structure, distributions, and correlations.
3. **Data Preprocessing:** Apply one-hot encoding to categorical features and map gender values.
4. **Feature Scaling:** Apply StandardScaler to numerical and encoded features.
5. **Train-Test Split:** Divide the dataset into training and testing sets.
6. **Model Training:** Train and compare six classification algorithms.
7. **Model Evaluation:** Evaluate models using Accuracy and F1-score.
8. **Deployment:** Save the selected SVM model and preprocessing artifacts using Joblib and integrate them with Streamlit.

## 🖥️ Application Features

- Interactive Streamlit interface.
- Patient health parameter inputs.
- SVM-based heart disease prediction.
- Real-time prediction results.
- Simple and user-friendly interface.

## 📁 Project Structure

```text
Heart-Disease-Prediction/
│
├── heart_diseases.ipynb
├── app.py
├── heart.csv
│
├── svm_heart.pkl
├── scaler.pkl
├── columns.pkl
│
└── README.md
```

## 🛠️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd heart
```

### 3. Install dependencies

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn joblib
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 📈 Model Evaluation

The models are evaluated using:

- Accuracy Score
- F1 Score
- Confusion Matrix
- Classification Report

The SVM classifier was selected for integration into the Streamlit application.

## 🔮 Future Improvements

- Hyperparameter tuning for improved model performance.
- Cross-validation for more reliable evaluation.
- Improved feature engineering.
- Comparison of additional ensemble models.
- Better visualization of prediction results.
- Deployment with a more comprehensive user interface.

## ⚠️ Disclaimer

This project is developed for educational and machine learning experimentation purposes only.

Predictions are not medical diagnoses. Always consult a qualified healthcare professional for medical advice.

## 👨‍💻 Author

**Devansh**

Computer Science & Engineering Student

GitHub: [@code-crusader-dev](https://github.com/code-crusader-dev)

---

⭐ If you find this project interesting, consider giving it a star!
