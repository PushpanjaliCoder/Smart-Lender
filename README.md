# 🏦 Smart Lender

# 🤖 AI Powered Loan Prediction System

Smart Lender is a Flask-based Machine Learning web application that predicts loan approval status based on applicant details.

The system analyzes applicant information such as income, loan amount, credit history, and other details to provide loan eligibility prediction results.

---

## ✨ Features

- 📝 User-friendly loan prediction interface
- 📋 Applicant information input form
- 🤖 Machine Learning based loan approval prediction
- 🌲 Random Forest Classifier model
- ⚙️ Data preprocessing and model training
- 📊 Loan status result display (Approved / Rejected)
- 🌐 Flask based web application

---

## 📁 Project Structure

- `app.py` - Flask application and prediction endpoint
- `train_model.py` - Trains the Machine Learning model
- `loan.csv` - Loan dataset file
- `loan_prediction_model.pkl` - Saved trained model
- `requirements.txt` - Python dependencies
- `static/` - CSS, JavaScript and image assets
- `templates/` - HTML templates for web pages

---

## 🛠 Requirements

- Python 3.8+
- Flask
- Pandas
- NumPy
- Scikit-learn

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Training the Model

Run the training script:

```bash
python train_model.py
```

This will train the Machine Learning model and generate:

`loan_prediction_model.pkl`

---

## 🚀 Running the Application

Start the Flask server:

```bash
python app.py
```

Open the application in browser:

```text
http://127.0.0.1:5000
```

---

## 🤖 Machine Learning Algorithm

- 🌲 Random Forest Classifier

The model analyzes applicant details and predicts whether the loan application is approved or rejected.

---

## 👨‍💻 Authors

- Pushpanjali Katta
- Charan Paidipula
- Chayakrishna P

---

## 🎯 Future Enhancements

- ☁️ IBM Cloud Deployment
- 🗄 Database Integration
- 📈 Improved dataset for better accuracy
- 🔐 User Authentication System
- 🤖 Advanced Machine Learning models

---

## 📝 Notes

This project is developed for educational purposes as a Machine Learning based loan prediction system.
