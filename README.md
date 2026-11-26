# 🏥 Insurance Cost Prediction Using Machine Learning

## 📌 Project Overview

This project is an interactive **Insurance Cost Prediction Application** developed using Machine Learning and Streamlit.

The application predicts medical insurance charges based on customer details such as age, gender, BMI, number of children, smoking status, and residential region.

A Multiple Linear Regression model is trained using the Insurance dataset, and the trained model is deployed as a web application using Streamlit Community Cloud.

## 🚀 Live Application

**Try the application here:**

[Insurance Cost Prediction – Streamlit App](https://linear-regression---ml-latdt292ufkvk3hsnaynmz.streamlit.app/)

## 🎯 Project Objectives

- Analyze the insurance dataset.
- Perform data preprocessing and cleaning.
- Handle missing values and duplicate records.
- Convert categorical variables into numerical values.
- Apply feature scaling.
- Train a Linear Regression model.
- Evaluate model performance.
- Predict insurance charges for new customers.
- Deploy the trained model using Streamlit.

## 📂 Dataset Description

The project uses the `insurance.csv` dataset.

### Input Features

| Feature | Description |
|---|---|
| age | Age of the customer |
| sex | Gender of the customer |
| bmi | Body Mass Index |
| children | Number of children |
| smoker | Smoking status |
| region | Residential region |

### Target Variable

- **charges:** Medical insurance cost.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Google Colab
- GitHub

## ⚙️ Machine Learning Workflow

1. Dataset loading using Pandas.
2. Exploratory Data Analysis (EDA).
3. Duplicate and missing value handling.
4. Data visualization using histograms.
5. Categorical feature encoding using One-Hot Encoding.
6. Splitting data into training and testing sets.
7. Feature scaling using StandardScaler.
8. Model training using Linear Regression.
9. Model evaluation using regression metrics.
10. Saving the trained model using Joblib.
11. Deploying the application using Streamlit.

## 📊 Model Evaluation

The model is evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

These metrics help measure the prediction errors and model performance.

## 💻 Streamlit Application Features

Users can enter the following details:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region

After entering the details and clicking the Predict Insurance Charges button, the application displays the estimated medical insurance charges.

## 📁 Project Structure

```text
Linear-Regression---ML/
│
├── app (2).py
├── model.pkl
├── scaler.pkl
├── columns.pkl
├── requirements.txt
└── README.md
```

## 📦 Installation and Usage

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run "app (2).py"
```

The application will open in your browser.

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud and hosted through GitHub.

**Live Application:**  
https://linear-regression---ml-latdt292ufkvk3hsnaynmz.streamlit.app/

## ⚠️ Disclaimer

This application provides estimated insurance charges based on a trained Machine Learning model. Predictions are for educational and demonstration purposes only and should not be considered actual insurance quotations.

## 👩‍💻 Author

**Project developed as a Machine Learning project using Python and Streamlit.**

---

⭐ If you find this project useful, feel free to explore the repository and try the live application!
