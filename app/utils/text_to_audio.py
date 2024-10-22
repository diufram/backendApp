from gtts import gTTS

def text_to_audio(text, slow=False):
    tts = gTTS(text, lang='es', slow=slow)  # slow=False es más natural
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file
