from flask import render_template, Flask, request, send_file, jsonify
import tempfile
from text2speech import text2speech
from speech2text import speech2text
from groq_service import execute
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/process-audio", methods =["POST"])
def process_audio_data():
    try:
        audio_data = request.files['audio'].read()

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            temp_audio.write(audio_data)
            temp_audio.flush()

        text = speech2text(temp_audio.name)
        generated_answer = execute(f"Please answer to the question: {text}")
        generated_speech = text2speech(generated_answer)

        return send_file(generated_speech, mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/transcribe-audio", methods=["POST"])
def transcribe_audio():
    try:
        audio_data = request.files['audio'].read()

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
            temp_audio.write(audio_data)
            temp_audio.flush()

        text = speech2text(temp_audio.name)
        return text
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__=='__main__':
    app.run(debug = True, port = 8080)

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Welcome to the audio processing app."

# @app.route("/process-audio", methods=["POST"])
# def process_audio():
#     audio_data = request.files['audio'].read()

#     with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
#         temp_audio.write(audio_data)
#         temp_audio.flush()

#     text = speech2text(temp_audio.name)
#     generated_answer = execute(f"Please answer to the question: {text}")
#     generated_speech = text2speech(generated_answer)

#     return send_file(generated_speech, mimetype='audio/mpeg')

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)