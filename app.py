from modules.transcriber import transcribe_audio
from modules.summarizer import summarize_text
import os

def main():

    audio_file_path = r"E:\Projects\AI-Voice-Summarizer\audio_files\New_Year_Resolution.mp3"

    print("Checking if file exists...")
    print("File exists:", os.path.exists(audio_file_path)) 

    # Step -1 [Transcription] -------------------------------------------------->

    transcript, transcript_path = transcribe_audio(audio_file_path)

    print("Transcription Completed")
    print("Trnascription saved at:", transcript_path)
    print("Transcript preview:\n", transcript)

    # Step -2 [Summarization] -------------------------------------------------->
    summary, summary_path = summarize_text(transcript_path=transcript_path, 
                                           max_length=120, 
                                           min_length=30)


    print("\nSummary saved at:", summary_path)
    print("Summary preview:\n", summary)

if __name__ == "__main__":
    main()
