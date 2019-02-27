import pyaudio
import wave
import sys
import time
import random
from pydub import AudioSegment

N_OF_STREAMS = 10

p = pyaudio.PyAudio()

audio_params = {'format': p.get_format_from_width(2), 'channels':2, 'rate':8000, 'frames_per_buffer': 8000, 'output':True, 'start': False}

class Player:
    streams = []
    audio = []

    def __init__(self, get_clips):
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
            time.sleep(0.1)

    def stop_streams(self):
        for stream in self.streams:
            stream.stop_stream()
            
    def callback(self, in_data, frame_count, time_info, status):
        clips = [clip for clip in self.get_clips()]
        print(1)
#        if not clips:
        return (bytes([0 for x in range(8000)]), pyaudio.paContinue)
        return (random.choice(clips), pyaudio.paContinue)
