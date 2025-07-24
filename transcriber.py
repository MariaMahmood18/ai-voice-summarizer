"""
transcriber.py
--------------

This module handles audio transcription using OpenAI Whisper.
Optimized for deployment: returns in-memory transcript without saving files.

Usage:
    - Call transcribe_audio(audio_path) with the path to the audio file
    - Returns a string containing the transcript

Model used: Whisper 'base'

Author: Maria Mahmood
Date: July 2025
"""

import whisper
import os

# Load the whisper model once
model = whisper.load_model(name="base")

def transcribe_audio(audio_path):
    """
    Transcribes an audio file.

    Parameters:
        audio_path (str): Path to the input audio file

    Returns:
        transcript (str): The transcribed text
    """
    
    print(f"Transcribing {audio_path}...")

    # Normalize path for cross-platform compatibility
    audio_path = os.path.normpath(audio_path)
    audio_path = audio_path.encode('unicode_escape').decode()

    # Check if file exists and is not empty
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    if os.path.getsize(audio_path) == 0:
        raise ValueError("Audio file is empty.")

    try:
        results = model.transcribe(audio_path)
        transcript = results["text"]
        return transcript
    except Exception as e:
        print(f"[ERROR] Whisper transcription failed: {e}")
        raise RuntimeError("Transcription failed. Please upload a valid audio file.")
