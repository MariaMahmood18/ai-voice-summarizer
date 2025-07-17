"""
summarizer.py
-------------

This module summarizes long text using Hugging Face's DistilBART model.
Now enhanced to take a transcript file path, read the text, summarize it,
and save the summary in a summary folder.

Author: Maria Mahmood
Date: July 2025
"""

from transformers import pipeline
import os

# Load pretrained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Create a function that takes text as input and performs summarization
def summarize_text(transcript_path, max_length=120, min_length=30):
    """
    Summarize the input text at trasncript path using the hugging face pre-trained transformer model and save it.

    Parameters:
        transcript_path (str): The path to input text to summarize
        max_length (int): Maximum tokens in output (default: 120)
        min_length (int): Minimum tokens in output (default: 30)

    Returns:
        tuple:
            summary (str): The summary of input text
            summary_path (str): The path where the summary is saved


    """
    
    transcript_path = os.path.normpath(transcript_path)

    # Load the transcript text from path
    with open(transcript_path, "r") as f:
        text = f.read()

    # Summarize the text
    summary = summarizer(text, 
                         max_length=max_length, 
                         min_length=min_length, 
                         do_sample=False) # do_sample -> ensures every time same summary for a text is produced no randomness 
    
    summary_text = summary[0]["summary_text"]

    # Construct filename and path 
    summary_folder = "summary"
    os.makedirs(summary_folder, exist_ok=True)
    base_filename = os.path.basename(transcript_path).replace("_transcript.txt", "_summary.txt")
    summary_path = os.path.join(summary_folder, base_filename)

    # Save the summary 
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(summary_text)
    
    
    return summary_text, summary_path