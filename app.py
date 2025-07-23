import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text_from_string
import tempfile
import os

st.set_page_config(page_title="AI Voice Summarizer", layout="centered")

st.title("🎙️ AI Voice Summarizer")
st.markdown("Upload an audio file, and get a summarized transcript.")

# Upload Section
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
        tmp_file.write(uploaded_file.read())
        audio_path = tmp_file.name

    st.success("✅ File uploaded")

    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_path)
    st.success("✅ Transcription Complete")
    st.text_area("Transcript", transcript, height=300, disabled=True)

    with st.spinner("Summarizing..."):
        summary = summarize_text_from_string(transcript)
    st.success("✅ Summary Generated")
    st.text_area("Summary", summary, height=200, disabled=True)
    
    os.remove(audio_path)
