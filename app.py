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
    if uploaded_file.size == 0:
        st.error("❌ Uploaded file is empty. Please upload a valid audio file.")
    else:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(uploaded_file.read())
                audio_path = tmp_file.name

            if os.path.getsize(audio_path) == 0:
                st.error("❌ Failed to save audio. The file is empty after writing.")
            else:
                st.success("✅ File uploaded")

                with st.spinner("Transcribing..."):
                    try:
                        transcript = transcribe_audio(audio_path)
                        if not transcript.strip():
                            raise ValueError("Transcription failed or returned empty text.")
                    except Exception as e:
                        raise RuntimeError("Whisper transcription failed: " + str(e))

                st.success("✅ Transcription Complete")
                st.text_area("Transcript", transcript, height=300, disabled=True)

                with st.spinner("Summarizing..."):
                    summary = summarize_text_from_string(transcript)
                st.success("✅ Summary Generated")
                st.text_area("Summary", summary, height=200, disabled=True)

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")

        finally:
            try:
                if os.path.exists(audio_path):
                    os.remove(audio_path)
            except Exception as cleanup_err:
                st.warning(f"⚠️ Failed to clean up temporary file: {cleanup_err}")
