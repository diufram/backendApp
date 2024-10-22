import wave
import json
import os
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

def convert_to_wav(input_file):
    # Convierte el archivo de entrada a formato WAV (16 kHz, mono)
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_frame_rate(16000).set_channels(1)
    
    # Guardar el archivo WAV convertido temporalmente
    output_file = "temp_converted_audio.wav"
    audio.export(output_file, format="wav")
    
    return output_file

def transcribe_audio_vosk(audio_file_path):
    # Si el archivo no es WAV, lo convertimos a WAV
    if not audio_file_path.endswith('.wav'):
        print("Convirtiendo archivo a WAV...")
        audio_file_path = convert_to_wav(audio_file_path)
    
    # Cargar el modelo (asegúrate de poner la ruta correcta a tu modelo de Vosk)
    model = Model("vosk-model-small-es-0.42")
    
    # Abrir el archivo WAV
    with wave.open(audio_file_path, "rb") as wf:
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in [8000, 16000]:
            raise ValueError("Formato de audio no soportado. Debe ser WAV mono con 8kHz o 16kHz")
        
        recognizer = KaldiRecognizer(model, wf.getframerate())
        
        # Procesar el audio y transcribirlo
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                print(json.loads(result)["text"])
    
        # Obtener el último resultado de la transcripción
        final_result = recognizer.FinalResult()
        print("Texto transcrito (offline):", json.loads(final_result)["text"])
    
    # Si se creó un archivo temporal WAV, lo eliminamos después de la transcripción
    if audio_file_path == "temp_converted_audio.wav":
        os.remove(audio_file_path)

# Prueba con un archivo de audio (puede ser M4A, MP3, u otro formato)
transcribe_audio_vosk("a.m4a")
