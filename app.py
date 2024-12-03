from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask('AlzheimerMRIApp')

# Load the trained model
model = load_model('alzheimers_model.h5')

# Function to map prediction to class name
def names(number):
    if number == 0:
        return 'Non Demented'
    elif number == 1:
        return 'Mild Dementia'
    elif number == 2:
        return 'Moderate Dementia'
    elif number == 3:
        return 'Very Mild Dementia'
    else:
        return 'Error in Prediction'

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image provided'}), 400

    try:
        img = Image.open(io.BytesIO(file.read()))
        img = img.convert('RGB')
        img = img.resize((128, 128))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)

        # Make prediction
        res = model.predict(x)
        classification = np.argmax(res, axis=1)[0]
        confidence = res[0][classification] * 100

        return jsonify({
            'prediction': names(classification),
            'confidence': f'{confidence:.2f}%'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)