import vosk, pyaudio, io, os
from gtts import gTTS
from pydub import AudioSegment

os.environ["PATH"] += os.pathsep + "C:\\ffmpeg"
lang = 'fr'
model = vosk.Model('model')

chunk_size = 1024
sample_rate = 44100
channels = 1

kaldi_recognizer = vosk.KaldiRecognizer(model, sample_rate)

def create_stream(input=True):
    if input:
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=sample_rate,
            input=True,
            frames_per_buffer=chunk_size
        )
    else:
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=channels,
            rate=sample_rate,
            output=True
        )

        return stream

def synthetize_and_play(text):
    tts = gTTS(text=text, lang=lang)
    with io.BytesIO() as f:
        tts.write_to_fp(f)
        f.seek(0)
        audio = AudioSegment.from_file(f)
        audio = audio.set_frame_rate(sample_rate)
        audio = audio.set_channels(channels)
        audio = audio.set_sample_width(2)  # 16-bit audio
        data = audio.raw_data
    
    stream_out = create_stream(input=False)
    start = 0
    while start < len(data):
        stream_out.write(data[start:start+chunk_size])
        start += chunk_size
    stream_out.stop_stream()
    stream_out.close()

while True:
    text = input("Entrer le texte a synthetiser > ")
    synthetize_and_play(text)