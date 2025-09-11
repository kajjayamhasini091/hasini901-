from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_output):
    try:
        # Load video
        video = VideoFileClip(video_path)
        
        # Extract audio
        audio = video.audio
        if audio is None:
            print("❌ No audio track found in this video.")
            return

        # Save as mp3 or wav
        audio.write_audiofile(audio_output)
        print(f"✅ Audio saved as: {audio_output}")

    except Exception as e:
        print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    video_file = "sample_video.mp4"   # Replace with your video file
    output_file = "extracted_audio.mp3"  # Can also use "output.wav"
    
    extract_audio(video_file, output_file)
