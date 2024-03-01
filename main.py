from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

import numpy as np
from model import make_prediction, verify_input

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        # Get data from the POST rpyequest
        data = request.json
        print(data)

        verify = verify_input(data['no_of_preg'], 
                              data['Glucose'], 
                              data['BloodPressure'], 
                              data["SkinThickness"],
                              data["Insulin"],
                              data["BMI"],
                              data["DiabetesPedigreeFunction"],
                              data["Age"])
        if verify == "Okay":
            # # Make predictions using the loaded model
            predictions_proba = make_prediction(data['no_of_preg'], 
                                        data['Glucose'], 
                                        data['BloodPressure'], 
                                        data["SkinThickness"],
                                        data["Insulin"],
                                        data["BMI"],
                                        data["DiabetesPedigreeFunction"],
                                        data["Age"]) 

            # # Convert predictions to a JSON response
            response = {
                'Ok': "True",
                'pred': str(predictions_proba.argmax()),
                'proba': str(predictions_proba.max() * 100),
                'error': ""}
        else: 
            response = {
                'Ok': "True",
                'pred': "",
                'proba': "",
                'error': verify}

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e),
                        'Ok': "False",
                        'pred': "",
                        "proba": ""})

if __name__ == '__main__':
    app.run(debug=True)
