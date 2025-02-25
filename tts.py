from gtts import gTTS
from io import BytesIO
import pygame

def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)  # Save to memory instead of a file
    audio_buffer.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_buffer, "mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    sample_text = "Hello, this is an AI-generated voice summary."
    text_to_speech(sample_text)
