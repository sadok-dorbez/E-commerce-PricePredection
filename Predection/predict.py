from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the trained Decision Tree model and label encoder
with open('decision_tree_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('labelencoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

size_mapping = {'XXS': 0, 'XS': 1, 'S': 2, 'M': 3, 'L': 4, 'XL': 5, 'XXL': 6}
theme_mapping = {'summer': 0, 'autumn': 1, 'spring': 2, 'winter': 3}

@cross_origin()
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Process the input data
    units = data['units']
    shipped = 1 if data['shipped'] else 0  # Convert to 1 or 0 based on boolean value
    size = data['size']
    theme = data['theme']

    # Convert the text inputs to numerical labels
    size = size_mapping[size]
    theme = theme_mapping[theme]

    # Create a DataFrame from the input data
    input_data = {
        'quantity': [units],
        'shipping': [shipped],
        'size': [size],
        'theme': [theme]
    }

    input_df = pd.DataFrame(input_data)

    # Make predictions on the input data
    predicted_price = model.predict(input_df)

    # Return the predicted value as a JSON response
    return jsonify({'predicted_price': float(predicted_price[0])})

if __name__ == '__main__':
    app.run(debug=True, port=6000)
