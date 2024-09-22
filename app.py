# Importing the necessary libraries
import pandas as pd
from flask import request, Flask, jsonify
import joblib

# Initialize Flask application
app = Flask(__name__)

# Load the model (replace with your actual model path)
model = joblib.load('./src/models/speciesPrediction.pkl')

@app.route('/')
def speciesPrediction():
    """
    Endpoint for predicting the Iris species based on input features.
    """
    try:
        # Get JSON data from request
        data = request.json
        
        # Convert the input data into a pandas DataFrame
        df = pd.DataFrame(data["data"])
        
        # Ensure the DataFrame contains the expected columns for the Iris dataset
        df = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
        
        # Cast the columns to the appropriate data types
        df['sepal_length'] = df['sepal_length'].astype('float64')
        df['sepal_width'] = df['sepal_width'].astype('float64')
        df['petal_length'] = df['petal_length'].astype('float64')
        df['petal_width'] = df['petal_width'].astype('float64')
        
        # Prepare input for the model
        input_data = df.iloc[:, :]
        
        # Make predictions using the loaded model
        predictions = model.predict(input_data)
        
        # Convert numerical predictions to species names
        species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
        final_predictions = [{'Iris Species Prediction': pred} for pred in predictions]
        
        # Return the predictions as a JSON response
        return jsonify(final_predictions)
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
