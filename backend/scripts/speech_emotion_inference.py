# import tensorflow as tf
# import librosa
# import numpy as np

# # Load Model
# model_path = "../models/speech_emotion_model.h5"
# model = tf.keras.models.load_model(model_path)

# # Emotion Mapping
# emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# # Inference Function
# def predict_speech_emotion(audio_path):
#     features = extract_features(audio_path)
#     if features is None:
#         return "Error: Unable to process audio file."

#     features = np.expand_dims(features, axis=0)
#     prediction = model.predict(features)
#     emotion = emotion_labels[np.argmax(prediction)]
#     return emotion

# # Example
# audio_path = "test_audio.wav"  # Replace with the path to your test audio
# emotion = predict_speech_emotion(audio_path)
# print(f"Predicted Emotion: {emotion}")




import tensorflow as tf
import librosa
import numpy as np

# Load Model
model_path = "./backend/models/speech_emotion_model.h5"  # Adjust path as necessary
model = tf.keras.models.load_model(model_path)

# Emotion Mapping
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Feature Extraction Function
def extract_features(file_path, max_pad_len=174):
    try:
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        pad_width = max_pad_len - mfccs.shape[1]
        mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        return mfccs
    except Exception as e:
        print(f"Error extracting features: {e}")
        return None

# Inference Function
def predict_speech_emotion(audio_path):
    features = extract_features(audio_path)
    if features is None:
        return "Error: Unable to process audio file."

    features = np.expand_dims(features, axis=0)  # Add batch dimension
    prediction = model.predict(features)
    emotion = emotion_labels[np.argmax(prediction)]
    return emotion

# Example
if __name__ == "__main__":
    audio_path = "test_audio.wav"  # Replace with a valid test audio path
    emotion = predict_speech_emotion(audio_path)
    print(f"Predicted Emotion: {emotion}")

