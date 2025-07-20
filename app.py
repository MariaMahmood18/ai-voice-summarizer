from modules.transcriber import transcribe_audio
from modules.summarizer import summarize_text
from modules.language_detector import detect_language
from modules.translator import translate
import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def main():
    audio_file_path = r"E:\Projects\AI-Voice-Summarizer\audio_files\Urdu.mp3"

    print("Checking if file exists...")
    print("File exists:", os.path.exists(audio_file_path))

    # Step 1 - Transcription
    transcript, transcript_path = transcribe_audio(audio_file_path)
    print("\nTranscription Completed")
    print("Transcript saved at:", transcript_path)
    print("Transcript preview:\n", transcript[:500])  # only preview first 500 characters

    # Step 2 - Language Detection
    language = detect_language(transcript)
    print(f"\nDetected language: {language}")

    if language == "unsupported":
        print("[ERROR] Language not supported. Exiting.")
        return

    # Step 3 - Translate to English if needed
    if language != "en":
        print(f"Translating transcript from {language} to English...")
        transcript = translate(transcript, src_lang=language, tgt_lang="en")
        
        # Save translated transcript temporarily
        transcript_path = transcript_path.replace(".txt", "_translated.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript)
        print("Translated transcript saved at:", transcript_path)

    # Step 4 - Summarization
    summary, summary_path = summarize_text(transcript_path=transcript_path)
    print("\nSummary saved at:", summary_path)
    print("Summary preview:\n", summary[:500])

    # Step 5 - Translate summary back to original language
    if language != "en":
        print(f"Translating summary back to {language}...")
        translated_summary = translate(summary, src_lang="en", tgt_lang=language)

        # Save final translated summary
        translated_summary_path = summary_path.replace(".txt", f"_translated_{language}.txt")
        with open(translated_summary_path, "w", encoding="utf-8") as f:
            f.write(translated_summary)

        print("Translated summary saved at:", translated_summary_path)
        print("Translated Summary preview:\n", translated_summary)

if __name__ == "__main__":
    main()

