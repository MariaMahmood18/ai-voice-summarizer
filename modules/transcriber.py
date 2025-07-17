"""
transcriber.py
--------------

This module handles audio transcription using OpenAI Whisper.
It loads the Whisper model once and provides a function to convert an audio file (.wav, .mp3, etc.)
into plain text transcription.
It supports both file-based saving and lightweight in-memory transcription
for deployment (e.g. Gradio, Streamlit, APIs).

Usage:
    - Call transcribe_audio(audio_path) with the path to the audio file
    - Returns a string containing the transcript

Model used: Whisper 'medium'

Author: Maria Mahmood
Date: July 2025
"""


import whisper
import os
import re

# Load the whisper medium model for speech recognition
model = whisper.load_model(name="medium")

# Create a function that takes an audio file path and returns its transcrpts as text
def transcribe_audio(audio_path, output_folder="transcripts"):
    """
    Transcribes an audio file and saves the text to output folder.

    Parameters:
        audio_path (str): Path to the input audio file
        output_folder: Folder where the transcript is to be stored (default: "transcripts")

    Returns:
        tuple:
            transcript (str): The transcribed text
            output_path (str): Path where the transcript file was saved
    """

    # Create output folder if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    print(f"Transcribing {audio_path}.......")

    audio_path = os.path.normpath(audio_path)
    audio_path = audio_path.encode('unicode_escape').decode()

    # Transcribe the audio using the loaded model
    results = model.transcribe(audio_path)

    # Extract the transcribed text from results dictionary
    transcript = results["text"]

    # Create output file name
    filename = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = os.path.join(output_folder, f"{filename}_transcript.txt")

    # Save transcript to a .txt file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript, output_path 