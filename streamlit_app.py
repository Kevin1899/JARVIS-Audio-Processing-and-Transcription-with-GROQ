# import streamlit as st
# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile as wav
# import requests
# import tempfile
# import time

# st.title("Audio Processing App")
# st.write("Press the button below to record audio from your microphone.")

# # Slider for selecting recording duration
# duration = st.slider("Select recording duration (seconds)", 1, 20, 5)
# # Sample rate for recording
# sample_rate = 44100

# def record_audio(duration):
#     st.write("Recording...")
#     progress_bar = st.progress(0)
#     audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
#     for i in range(duration):
#         time.sleep(1)
#         progress_bar.progress((i + 1) / duration)
#     sd.wait()  # Wait until recording is finished
#     st.write("Recording finished.")
#     progress_bar.empty()
#     return audio_data

# if st.button("Record Audio"):
#     audio_data = record_audio(duration)
    
#     # Save the recorded audio temporarily
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
#         wav.write(temp_file.name, sample_rate, audio_data)
#         temp_file_path = temp_file.name

#     st.write("Sending audio to server for processing...")
    
#     # Send the recorded audio to the Flask backend
#     with open(temp_file_path, 'rb') as file:
#         response = requests.post("http://localhost:8080/process-audio", files={"audio": file})

#     if response.status_code == 200:
#         st.write("Audio processed successfully!")
#         st.audio(response.content, format="audio/mpeg")
#     else:
#         st.write(f"Failed to process the audio file. Status code: {response.status_code}")



import streamlit as st
import streamlit.components.v1 as components

st.title("Audio Processing App with Waveform Visualization")

# Load the HTML file
with open(r"C:\Users\TRPL\Desktop\JARVIS\templates\index1.html", "r") as f:
    html_code = f.read()

# Embed the HTML into Streamlit app
components.html(html_code, height=600)

