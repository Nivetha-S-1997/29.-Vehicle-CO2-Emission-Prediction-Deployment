from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
# Load the pre-trained model
filename = 'Final_model_randomforest.sav'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input features from form
        Engine_Size = float(request.form['engine size'])
        Combined_Fuel_Consumption = float(request.form['fuel consumption combined'])

        # Format the input data into a numpy array
        input_data = np.array([[Engine_Size, Combined_Fuel_Consumption]])

        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        print(prediction)
        
        return render_template('output.html', result=round(float(prediction[0]), 2))
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
