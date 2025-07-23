"""
summarizer.py
-------------
This module generates summaries from transcripts using Hugging Face's BART model.
Uses sentence-aware chunking, two-pass summarization, and basic cleanup for more readable summaries.

Author: Maria Mahmood
Date: July 2025
"""

import os
import warnings
import spacy
import re
from transformers import pipeline, AutoTokenizer

warnings.filterwarnings("ignore")

# Load spaCy English model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("[INFO] spaCy model not found. Installing...")
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Initialize BART summarization pipeline
model_name = "facebook/bart-large-cnn"
summarizer = pipeline("summarization", model=model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def sentence_based_chunks(text, max_words=100):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    chunks, current_chunk, current_len = [], [], 0
    for sent in sentences:
        word_len = len(sent.split())
        if current_len + word_len <= max_words:
            current_chunk.append(sent)
            current_len += word_len
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent]
            current_len = word_len
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def dynamic_summarize(chunk, min_length=30, ratio=0.25, max_cap=120):
    input_len = len(chunk.split())
    max_len = min(max(int(input_len * ratio), min_length), max_cap)

    result = summarizer(chunk, max_length=max_len, min_length=min_length, do_sample=False)
    summary = result[0]['summary_text']
    return clean_summary(summary)

def clean_summary(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"(\.\.\.|--)\s*", ".", text)
    text = re.sub(r"\s*([.,!?])", r"\1", text)

    sentences = [s.strip() for s in re.split(r'(?<=[.!?]) +', text)]
    seen = set()
    filtered = []
    for s in sentences:
        if len(s.split()) > 4 and s not in seen:
            filtered.append(s)
            seen.add(s)
    return " ".join(filtered)

def summarize_text_from_string(input_text, max_cap=120, min_length=30, two_pass=True):
    text = input_text.strip()
    word_count = len(text.split())

    if word_count > 200:
        chunks = sentence_based_chunks(text, max_words=120)
        first_pass = []
        for i, chunk in enumerate(chunks):
            try:
                summary = dynamic_summarize(chunk, min_length=min_length, ratio=0.25, max_cap=max_cap)
                first_pass.append(summary)
            except Exception as e:
                print(f"[ERROR] First-pass summarization failed at chunk {i}: {e}")
                first_pass.append("")

        combined_summary = " ".join(first_pass)
    else:
        try:
            combined_summary = dynamic_summarize(text, min_length=min_length, ratio=0.25, max_cap=max_cap)
        except Exception as e:
            print(f"[ERROR] Direct summarization failed: {e}")
            combined_summary = "[Error in summarization]"

    if two_pass:
        tokenized_len = len(tokenizer.encode(combined_summary, truncation=False))
        if tokenized_len > 1024:
            try:
                final_summary = dynamic_summarize(combined_summary, min_length=min_length, ratio=0.3, max_cap=max_cap)
            except Exception as e:
                print(f"[ERROR] Second-pass summarization failed: {e}")
                final_summary = combined_summary
        else:
            final_summary = combined_summary
    else:
        final_summary = combined_summary

    # --- COMMENTED FOR DEPLOYMENT ---
    # summary_folder = "summary"
    # os.makedirs(summary_folder, exist_ok=True)
    # base_filename = os.path.basename(transcript_path).replace("_transcript.txt", "_summary.txt")
    # summary_path = os.path.join(summary_folder, base_filename)
    # with open(summary_path, "w", encoding="utf-8") as f:
    #     f.write(final_summary.strip())

    return final_summary.strip()
