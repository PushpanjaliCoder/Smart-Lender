from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load trained model
model = joblib.load("loan_prediction_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Gender
    gender = 1 if request.form["gender"] == "Male" else 0

    # Married
    married = 1 if request.form["married"] == "Yes" else 0

    # Dependents
    dep = request.form["dependents"]

    if dep == "0":
        dependents = 0
    elif dep == "1":
        dependents = 1
    elif dep == "2":
        dependents = 2
    else:
        dependents = 3

    # Education
    education = 1 if request.form["education"] == "Graduate" else 0

    # Applicant Income
    income = int(request.form["income"])

    # Coapplicant Income
    coincome = int(request.form["coincome"])

    # Loan Amount
    loan = int(request.form["loan"])

    # Loan Amount Term
    loanterm = int(request.form["loanterm"])

    # Credit History
    credit = 1 if request.form["credit"] == "Good" else 0

    # Self Employed
    selfemployed = 1 if request.form["selfemployed"] == "Yes" else 0

    # Property Area
    property = request.form["property"]

    if property == "Rural":
        property = 0
    elif property == "Semiurban":
        property = 1
    else:
        property = 2

    features = [[
        gender,
        married,
        dependents,
        education,
        income,
        coincome,
        loan,
        loanterm,
        credit,
        selfemployed,
        property
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        result = "✅ Loan Approved"
    else:
        result = "❌ Loan Rejected"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)