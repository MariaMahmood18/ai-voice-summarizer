"""
transcriber.py
--------------

This module handles audio transcription using OpenAI Whisper.
Optimized for deployment: returns in-memory transcript without saving files.

Usage:
    - Call transcribe_audio(audio_path) with the path to the audio file
    - Returns a string containing the transcript

Model used: Whisper 'medium'

Author: Maria Mahmood
Date: July 2025
"""

import whisper
import os

# Load the whisper medium model
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

    audio_path = os.path.normpath(audio_path)
    audio_path = audio_path.encode('unicode_escape').decode()

    results = model.transcribe(audio_path)
    transcript = results["text"]

    # --- Removed file saving for deployment ---
    # filename = os.path.splitext(os.path.basename(audio_path))[0]
    # output_path = os.path.join("transcripts", f"{filename}_transcript.txt")
    # os.makedirs("transcripts", exist_ok=True)
    # with open(output_path, "w", encoding="utf-8") as f:
    #     f.write(transcript)

    return transcript
