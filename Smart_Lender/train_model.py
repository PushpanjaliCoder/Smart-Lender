import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv("loan.csv")

# Convert text into numbers
data["Gender"] = data["Gender"].map({"Male":1,"Female":0})
data["Married"] = data["Married"].map({"Yes":1,"No":0})
data["Loan_Status"] = data["Loan_Status"].map({"Y":1,"N":0})

# Inputs
X = data[["Gender","Married","ApplicantIncome","LoanAmount","CreditHistory"]]

# Output
y = data["Loan_Status"]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# Save model
joblib.dump(model,"loan_prediction_model.pkl")

print("Model Trained Successfully!")