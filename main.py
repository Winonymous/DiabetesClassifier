from flask import Flask, jsonify, request, render_template
from model import make_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the POST rpyequest
        data = request.json
        print(data)
        # # Make predictions using the loaded model
        predictions = make_prediction(data['no_of_preg'], 
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
            'pred': str(predictions),
            'error': ""}

        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e),
                        'Ok': "False",
                        'pred': ""})

if __name__ == '__main__':
    app.run(debug=True)
