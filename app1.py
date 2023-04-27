from flask import Flask, render_template, request
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
app = Flask(__name__)


# load the model
model = joblib.load("credit_risk_classification.joblib")

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/predict", methods=["POST"])
def predict():
    # get the input values from the form
    int_rate = float(request.form["int_rate"])
    grade = request.form["grade"]
    home_ownership = request.form["home_ownership"]
    purpose = request.form["purpose"]
    verification_status = request.form["verification_status"]
    mths_since_issue_d = float(request.form["mths_since_issue_d"])
    out_prncp = float(request.form["out_prncp"])
    total_rec_late_fee = float(request.form["total_rec_late_fee"])
    recoveries = float(request.form["recoveries"])

    # perform one hot encoding on grade
    # perform one hot encoding on grade and verification_status
    if grade == 'A':
        grade_A = 1
        grade_B = 0
        grade_C = 0
        grade_D = 0
        grade_E = 0
        grade_F = 0
        grade_G = 0
    elif grade == 'B':
        grade_A = 0
        grade_B = 1
        grade_C = 0
        grade_D = 0
        grade_E = 0
        grade_F = 0
        grade_G = 0
    elif grade == 'C':
        grade_A = 0
        grade_B = 0
        grade_C = 1
        grade_D = 0
        grade_E = 0
        grade_F = 0
        grade_G = 0
    elif grade == 'D':
        grade_A = 0
        grade_B = 0
        grade_C = 0
        grade_D = 1
        grade_E = 0
        grade_F = 0
        grade_G = 0
    elif grade == 'E':
        grade_A = 0
        grade_B = 0
        grade_C = 0
        grade_D = 0
        grade_E = 1
        grade_F = 0
        grade_G = 0
    elif grade == 'F':
        grade_A = 0
        grade_B = 0
        grade_C = 0
        grade_D = 0
        grade_E = 0
        grade_F = 1
        grade_G = 0
    elif grade == 'G':
        grade_A = 0
        grade_B = 0
        grade_C = 0
        grade_D = 0
        grade_E = 0
        grade_F = 0
        grade_G = 1    
        
    if verification_status == 'Not Verified':
       Status_Not_Verified = 1
       Status_Source_Verified = 0
       Status_Verified = 0
    elif verification_status == 'Verified':
       Status_Not_Verified = 0
       Status_Source_Verified = 0
       Status_Verified = 1
    else:
       Status_Not_Verified = 0
       Status_Source_Verified = 1
       Status_Verified = 0
       
    if home_ownership == 'Mortgage':
       Home_MORTGAGE = 1
       Home_NONE = 0
       Home_OTHER = 0
       Home_OWN = 0
       Home_RENT = 0
    elif home_ownership == 'None':
       Home_MORTGAGE = 0
       Home_NONE = 1
       Home_OTHER = 0
       Home_OWN = 0
       Home_RENT = 0
    elif home_ownership == 'Other':
       Home_MORTGAGE = 0
       Home_NONE = 0
       Home_OTHER = 1
       Home_OWN = 0
       Home_RENT = 0
    elif home_ownership == 'Own':
       Home_MORTGAGE = 0
       Home_NONE = 0
       Home_OTHER = 0
       Home_OWN = 1
       Home_RENT = 0
    elif home_ownership == 'Rent':
       Home_MORTGAGE = 0
       Home_NONE = 0
       Home_OTHER = 0
       Home_OWN = 0
       Home_RENT = 1
     
    if purpose == 'Car':
       Purpose_car = 1
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Credit_card':
       Purpose_car = 0
       Purpose_credit_card = 1
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Debt_consolidation':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 1
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Educational':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 1
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Home_improvement':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 1
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'House':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 1
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Major_purchase':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 1
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Medical':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 1
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Moving':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 1
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Other':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 1
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Renewable_energy':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 1
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Small_business':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 1
       Purpose_vacation = 0
       Purpose_wedding = 0
    elif purpose == 'Vacation':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 1
       Purpose_wedding = 0
    elif purpose == 'Wedding':
       Purpose_car = 0
       Purpose_credit_card = 0
       Purpose_debt_consolidation = 0
       Purpose_educational = 0
       Purpose_home_improvement = 0
       Purpose_house = 0
       Purpose_major_purchase = 0
       Purpose_medical = 0
       Purpose_moving = 0
       Purpose_other = 0
       Purpose_renewable_energy = 0
       Purpose_small_business = 0
       Purpose_vacation = 0
       Purpose_wedding = 1
       
    X = np.array([[grade_A, grade_B, grade_C, grade_D, grade_E, grade_F, grade_G, Status_Not_Verified, Status_Source_Verified, Status_Verified, 
                   Home_MORTGAGE, Home_NONE, Home_OTHER, Home_OWN, Home_RENT, Purpose_car, Purpose_credit_card, Purpose_debt_consolidation, Purpose_educational, Purpose_home_improvement,
                   Purpose_house, Purpose_major_purchase, Purpose_medical, Purpose_moving, Purpose_other, Purpose_renewable_energy, Purpose_small_business, Purpose_vacation,
                   Purpose_wedding, int_rate, out_prncp, total_rec_late_fee, recoveries, mths_since_issue_d]], dtype=object)
     
    # make a prediction
    prediction = model.predict(X)

    # return the prediction result as a string
    if prediction == 0:
        message = "Credit risk is good"
        image_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheeICCHOdB-IEpE4ahIdhOAobQbJcf4zmaGg6vfEdfhdhBYrqtmYOLHx7duHZVIPr0GlXsUllG5VvfZCRMEyp7K_FbAYeq_N5kz0HwsZo7lfrajA7gHklDyG30nRPecayYPLkhzy3bZSuDUy4bakb1XuNGJFG6fCXab-64Cn3t21Z-0Psiotf9F5VB/s346/goodcredit-2.jpg"
    elif prediction == 1:
        message = "Credit risk is bad"
        image_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYr83NOnS-WU7cIrgZSKWxw0ALXA5xFY8brgIxze-Ojk_ye-KX1zedttVbr6UoyH7zBrH40GrmOZJ3QXTTXSuX3tMwZQbkvwkn0zWA6Ex5pn7pGbnYxGnZRlsVhoLqUtt650v6nHA2s1_E5bEO4J8wzTlpfvgTycD7nUI5dXXbgdFOqiXgWZlpeFN0/s768/Bad-Credit.png"
    return render_template('result.html', image_url=image_url, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
