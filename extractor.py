import numpy as np
import pyaudio, math, random
import wave
from view import root
FRAMES_PER_SECOND = 10

class Point:
        def __init__(self, shift, p_avg, clips, randomClips):
                self.shift = shift
                self.p_avg = p_avg
                self.clips = randomClips + [clips]
                self.x = shift
                self.y = p_avg
        def dist(self, x, y):
                return math.sqrt((x - self.x)**2 + (y - self.y)**2)


def read_file(filename):
        file = open(filename, "r")
        samples = []
        for line in file:
                samples.append(line.split())
        samples = np.array(samples, dtype=float)
        return samples[:,0]

        
def extract_features(soundfile, snackfile):
        print("reading file: " + soundfile)
        l = 500
        seconds = 420
        sound = wave.open(soundfile, 'rb')
        samples = read_file(snackfile)
        points = []
        clips = segment(sound, FRAMES_PER_SECOND, seconds)
        sound.close()
        p_shift = pitch_shift(samples, l, seconds)
        p_avg = pitch_average(samples, l, seconds)
        for i in range(len(p_shift)):
                if p_shift[int(i)] < 0 or p_avg[int(i)] < 0:
                        continue
                points.append(Point(490*p_shift[int(i/5)], 490*p_avg[int(i/5)], clips[i:i+5], get_random_clips(clips)))
                
        return points

def get_random_clips(clips):
        randomClips = [[random.choice(clips) for i in range(5)] for i in range(3)]
        return randomClips

def segment(data, l, seconds):
        sample_rate = 3200
        d = np.array(list(data.readframes(l*sample_rate))).astype(np.int8)
        fade = 8464
        fadein = np.arange(0., 1., 1/fade).astype(np.float32)
        fadeout = np.arange(1., 0., -1/fade).astype(np.float32)
        clip = []
        read = 0
        while len(d) > fade and read <= seconds:
                d[:fade] = np.multiply(d[:fade], fadein)
                d[-fade:] = np.multiply(d[-fade:], fadeout)
                clip.append(bytes(np.array(d).astype(np.uint8)))
                d = np.array(list(data.readframes(l*sample_rate))).astype(np.int8)
                read += 1
        return clip


def pitch_average(samples, l, seconds):
        avg_pitch = []
        for i in range(0,min(len(samples), seconds * 100),l):
                try:
                        slice = [s for s in samples[i:i+l] if s > 0]
                        p = np.mean(slice) if len(slice) > 0 else 1
                        if p < 1:
                              p = 1 
                        avg_pitch.append(np.log(p))
                except:
                        avg_pitch.append(0)
        
        high = max(avg_pitch)
        low = min([p for p in avg_pitch if p > 0])
        return (np.array(avg_pitch) - low) / (high - low)

	
def pitch_shift(samples, l, seconds):
        shift = []
        for i in range(0,min(len(samples), seconds * 100),l):
                try:
                        p = max(samples[i:i+l]) - min([s for s in samples[i:i+l]if s > 0])
                        if p < 1:
                                p = 1
                        shift.append(np.log(p))
                except:
                        shift.append(0)

        high = max(shift)
        low = min([p for p in shift if p > 0])
        return (np.array(shift) - low) / (high - low)

