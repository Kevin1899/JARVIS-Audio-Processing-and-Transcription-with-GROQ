# JARVIS Audio Processing and Transcription with GROQ

This project leverages advanced audio processing capabilities combined with GROQ's cutting-edge AI technology to create an intelligent system for real-time audio transcription and response generation. This project involves several key components:

## Features

1. **Real-time Audio Recording**: Users can record audio directly through a web interface, utilizing real-time feedback and progress indicators.
2. **Waveform Visualization**: Visual representation of audio input with a real-time waveform that goes up and down as you speak.
3. **Audio Processing**: The recorded audio is sent to a Flask backend where it undergoes noise reduction, echo cancellation, and voice modulation to enhance quality.
4. **Transcription Service**: The processed audio is transcribed into text using sophisticated speech-to-text algorithms powered by GROQ.
5. **AI-Driven Responses**: GROQ's AI models generate meaningful responses based on the transcribed text, offering a conversational experience.
6. **User Interface**: A user-friendly interface built with Streamlit allows seamless interaction, playback of processed audio, and display of transcriptions.

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/jarvis-audio-processing.git
cd jarvis-audio-processing
```
2. **Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Set Up Environment Variables**
Create a .env file in the root directory and add your API keys and other necessary environment variables:
```bash
GROQ_API_KEY=your_groq_api_key
DG_API_KEY=your_deepgram_api_key
```
5. **Running the Application**
Start Flask Backend
```bash
python app.py
```
6. **Run Streamlit App**
```bash
streamlit run streamlit_app.py
```

# Usage
- Open your browser and go to http://localhost:8501 to access the Streamlit app.
- Press the "Record Audio" button to start recording.
- Watch the waveform visualization as you speak.
- Press the "Stop Recording" button to stop recording.
- Press the "Send Audio" button to process the audio and view the transcription.

## Project Structure
```bash
.
├── app.py                     # Flask backend server
├── streamlit_app.py           # Streamlit frontend application
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── templates/
│   └── index.html             # HTML template for the frontend
└── static/
    └── main.js                # JavaScript for recording and visualizing audio
```
## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch).
5. Create a new Pull Request.
