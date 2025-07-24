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

if "transcript" not in st.session_state:
    st.session_state.transcript = None
if "summary" not in st.session_state:
    st.session_state.summary = None

if uploaded_file:
    if uploaded_file.size == 0:
        st.error("❌ Uploaded file is empty. Please upload a valid audio file.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
            tmp_file.write(uploaded_file.read())
            audio_path = tmp_file.name

        st.success("✅ File uploaded")

        if st.session_state.transcript is None:
            try:
                with st.spinner("Transcribing..."):
                    transcript = transcribe_audio(audio_path)
                    st.session_state.transcript = transcript
                st.success("✅ Transcription Complete")
            except Exception as e:
                st.error(f"❌ Transcription Error: {str(e)}")
                os.remove(audio_path)
                st.stop()

        st.text_area("Transcript", st.session_state.transcript, height=300, disabled=True)

        if st.session_state.summary is None:
            with st.spinner("Summarizing..."):
                summary = summarize_text_from_string(st.session_state.transcript)
                st.session_state.summary = summary
            st.success("✅ Summary Generated")

        st.text_area("Summary", st.session_state.summary, height=200, disabled=True)

        try:
            os.remove(audio_path)
        except:
            pass
