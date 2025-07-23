import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text_from_string
from transformers import pipeline
import os

st.set_page_config(page_title="AI Voice Summarizer", layout="centered")

st.title("🎙️ AI Voice Summarizer")
st.markdown("Upload an audio file, and get a summarized transcript.")

# Upload Section
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with st.spinner("Saving audio file..."):
        audio_path = f"temp_audio.{uploaded_file.name.split('.')[-1]}"
        with open(audio_path, "wb") as f:
            f.write(uploaded_file.read())

    st.success("✅ File uploaded")

    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_path)
    st.success("✅ Transcription Complete")
    st.text_area("Transcript", transcript, height=250)

    with st.spinner("Summarizing..."):
        summary = summarize_text_from_string(transcript)
    st.success("✅ Summary Generated")
    st.text_area("Summary", summary, height=200)

    # Cleanup
    os.remove(audio_path)
