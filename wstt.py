#! /usr/bin/env python3

## STT - Whisper AI

# imports
import os
import sounddevice as sd
from scipy.io.wavfile import write
import whisper

# voice recording
def record():
    sample_rate = 16000
    duration = 9
    # record start
    recording = sd.rec(int(duration *sample_rate),
                           samplerate=sample_rate,
                           channels=1)
    sd.wait()

    # outputs audio in file
    write("output_whisper.wav", sample_rate, recording)
    whisp()

# whisper func
def whisp():
    audio = os.path.abspath("output_whisper.wav")
    # Models
    # tiny - base - small - medium
    m = whisper.load_model("small")
    
    # transcribe audio
    text = whisper.transcribe(model=m,audio=audio)
    print(text['text'])
    
    delete_file(audio)

# deletes file
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("no file")

def main():
    record()

if __name__ == "__main__":
    main()