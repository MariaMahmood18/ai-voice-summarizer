---
title: AI Voice Summarizer
emoji: 🗣️📄
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
pinned: false
---

# 🗣️ AI Voice Summarizer

AI Voice Summarizer is a simple and powerful Streamlit-based web app that converts your **audio into text** and provides a **concise summary** — in just seconds!

> Powered by OpenAI Whisper, Hugging Face Transformers, Streamlit, and deployed on Hugging Face Spaces.

---

## Demo

🎬 [Watch Demo Video on YouTube](https://www.youtube.com/watch?v=xFNtoHJYJ98)

---

## Features

- Upload `.mp3`, `.wav`, or `.m4a` audio files
- Transcribe speech to text using **Whisper**
- Summarize the transcription using **BART** (`facebook/bart-large-cnn`)
- Intuitive and responsive web interface (Streamlit)
- Deployed on Hugging Face Spaces

---

## Tech Stack

| Component        | Tool                                 |
|------------------|--------------------------------------|
| Transcription    | OpenAI Whisper (base model)          |
| Summarization    | Hugging Face Transformers (BART)     |
| Frontend         | Streamlit                            |
| Deployment       | Hugging Face Spaces                  |
| Programming Lang | Python                               |

---

##  How It Works

1. **Upload** an audio file (`.mp3`, `.wav`, `.m4a`)
2. The app uses **Whisper** to **transcribe** it to plain text
3. The transcribed text is passed to **BART** to generate a **summary**
4. Results are displayed in two separate boxes

---

## Run Locally (Main Branch)

### 🔧 Requirements

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/download.html) installed and in system PATH
- Git installed

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/ai-voice-summarizer.git
cd ai-voice-summarizer

# (Optional) Set up a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install required packages
pip install -r requirements.txt
```

###  Launch the App

```bash
streamlit run app.py
```


