# from flask import Flask
# from routes.face_emotion import face_emotion_bp
# from routes.speech_emotion import speech_emotion_bp
# from routes.response_system import response_bp


# app = Flask(__name__)

# # Register blueprints
# app.register_blueprint(face_emotion_bp, url_prefix="/api/face")
# app.register_blueprint(speech_emotion_bp, url_prefix="/api/speech")
# app.register_blueprint(response_bp, url_prefix="/api/response")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from routes.face_emotion import face_emotion_bp
from routes.speech_emotion import speech_emotion_bp
from routes.response_system import response_bp
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
from firebase_config import db  # Import the Firebase Firestore client

app = Flask(__name__)

# Register blueprints
app.register_blueprint(face_emotion_bp, url_prefix="/api/face")
app.register_blueprint(speech_emotion_bp, url_prefix="/api/speech")
app.register_blueprint(response_bp, url_prefix="/api/response_system")

if __name__ == "__main__":
    app.run(debug=True)