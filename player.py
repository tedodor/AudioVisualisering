import pyaudio
import wave
import sys
import time
import random

N_OF_STREAMS = 10
CLIP_SIZE = 1

p = pyaudio.PyAudio()

audio_params = {'format': p.get_format_from_width(2), 'channels':1, 'rate':32000, 'frames_per_buffer': 32000, 'output':True, 'start': False}

class Player:
    streams = []
    audio = []

    def __init__(self, get_clips):
        silenceclip = wave.open("rsc/silence.wav", 'rb')
        self.silence = silenceclip.readframes(44100)
        self.get_clips = get_clips
        self.init_streams()
        self.start_streams()
    
    def init_streams(self):
        audio_params['stream_callback'] = self.callback
        for s in range(N_OF_STREAMS):
            self.streams.append(p.open(
                **audio_params))

    def start_streams(self):
        for stream in self.streams:
            stream.start_stream()
            time.sleep(CLIP_SIZE/N_OF_STREAMS)

    def stop_streams(self):
        for stream in self.streams:
            stream.stop_stream()
            
    def callback(self, in_data, frame_count, time_info, status):
        clips = [clip for clip in self.get_clips()]
        if not clips:
            return (self.silence, pyaudio.paContinue)
        return (random.choice(random.choice(clips)), pyaudio.paContinue)
