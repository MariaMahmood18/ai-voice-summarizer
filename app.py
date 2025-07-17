from modules.transcriber import transcribe_audio
import os

def main():

    audio_file_path = r"E:\Projects\AI-Voice-Summarizer\audio_files\harvard.wav"

    print("Checking if file exists...")
    print("File exists:", os.path.exists(audio_file_path)) 

    transcript, output_path = transcribe_audio(audio_file_path)

    print("Transcription Completed")
    print("Trnascription saved at:", output_path)
    print("Transcript preview:\n", transcript)

if __name__ == "__main__":
    main()
