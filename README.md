# Diabetes Prediction using Machine Learning

This project is a Machine Learning Classification application that predicts whether a person is diabetic or not based on medical attributes.

The project is built using:

- Python
- Scikit-learn
- Streamlit
- Gaussian Naive Bayes Algorithm

---

# Project Overview

The application uses the **Gaussian Naive Bayes Classification Algorithm** to classify patients as:

- Diabetic
- Non-Diabetic

The workflow includes:

1. Loading the dataset
2. Data preprocessing
3. Feature scaling using `StandardScaler`
4. Train-test splitting
5. Building a Machine Learning pipeline
6. Training the classification model
7. Saving the trained model
8. Deploying the application using Streamlit

---

# Project Structure

```bash
Diabetes-Classification/
│
├── diabetes.csv
├── train_model.py
├── app.py
├── diabetes_model.pkl
├── requirements.txt
└── README.md
