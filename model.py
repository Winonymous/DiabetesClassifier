import joblib
import pandas as pd

path = "./models/filename.joblib"

model = joblib.load(path) 

def make_prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
       BMI, DiabetesPedigreeFunction, Age):
    

    data = pd.DataFrame({'Pregnancies': [Pregnancies], 
                        'Glucose': [Glucose], 
                        'BloodPressure': [BloodPressure], 
                        'SkinThickness': [SkinThickness], 
                        'Insulin': [Insulin],
                        'BMI': [BMI], 
                        'DiabetesPedigreeFunction': [DiabetesPedigreeFunction], 
                        'Age': [Age]})
    
    prediction = model.predict_proba(data)[0]

    return prediction

print(make_prediction(6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0))

def verify_input(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
       BMI, DiabetesPedigreeFunction, Age):
    
    if (Pregnancies <= 17 and Pregnancies >= 0):
        if (Glucose <= 200 and Glucose >= 0):
            if (BloodPressure <= 130 and BloodPressure >= 0):
                if (SkinThickness <= 130 and SkinThickness >= 0):
                    if (Insulin <= 130 and Insulin >= 0):
                        if (BMI <= 130 and BMI >= 0):
                            if (DiabetesPedigreeFunction <= 3 and DiabetesPedigreeFunction >= 0):
                                if (Age > 20):
                                    return "Okay"
                                else:
                                    return "Age must be greater than 20"
                            else:
                                return "Invalid range DiabetesPedigreeFunction must be between 0 and 3"
                        else:
                            return "Invalid range BMI must be between 0 and 100"
                    else:
                        return "Invalid range Insulin must be between 0 and 200"
                else:
                    return "Invalid range SkinThickness must be between 0 and 100"
            else:
                return "Invalid range BloodPressure must be between 0 and 130" 
        else:
            return "Invalid range Glucose must be between 0 and 200" 
    else:
        return "Invalid range Pregnancies must be between 0 and 17" 
                

                