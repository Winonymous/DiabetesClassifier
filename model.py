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
    
    prediction = model.predict(data)[0]

    return prediction

print(make_prediction(6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0))
