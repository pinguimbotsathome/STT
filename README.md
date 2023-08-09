# STT
Speech-to-text using Whisper AI and sounddevice for PinguimBots.

## Why Whisper
Among all the tested Python libraries and APIs, Whisper stands out as the most accurate. Additionally, there is the matter of model loading. Even with larger models like ```small``` and ```medium```, Whisper's loading time is faster than that of the others.

### Tested python libraries
- **NeMo**
	- A lot of features
	- can be complicated to understand
	- loading of model is slow
	- accuracy depends on the model
	- Source code: https://github.com/NVIDIA/NeMo/tree/main
	- Tutoriais: https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/starthere/tutorials.html
	- NeMo: https://developer.nvidia.com/pt-br/nvidia-nemo
- **Whisper**
	- accurate
	- 5  diferent models -> 4 are English-only
	- can only do transcription in 30s audio
	- OpenAI: https://openai.com/research/whisper
	- Source code: https://github.com/openai/whisper
- **Vosk**
	- open-source
	- offline
	- 20+ languages
	- not accurate
	- Website/Docs: https://alphacephei.com/vosk/
	- Source code: https://github.com/alphacep/vosk-api/
- **Deepspeech**
	- open-source
	- uses TensorFlow
  - not very accurate
	- Docs: https://deepspeech.readthedocs.io/?badge=latest
	- Source code: https://github.com/mozilla/DeepSpeech?referral=stt-with-python
- **SpeechRecognition**
	- Suports many APIs and engines like Vosk e Whisper
	- accuracy depends on the APIs or engine used 
	- Pypi: https://pypi.org/project/SpeechRecognition/
	- Source code: https://github.com/Uberi/speech_recognition

## Install requirements
```bash
$ pip install -r requirements.txt
```
### How to run
```bash
$ git clone https://github.com/pinguimbotsathome/STT
$ cd STT
$ python wstt.py
```
### How the code works
First it records the audio with sounddevice and saves it locally using scipy. Then, the audio is transcribed with Whisper AI. After transcription, delete_file is called to delete the audio file.
#### Notes
Whisper can only transcribe a 30 second audio. Because of this, it was decided to save an audio file with a set duration for the transcription. The variable ```duration``` represents the max time of recording.
