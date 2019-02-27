import wave, pyaudio, random, time

CHUNK = 8000

wf = wave.open("rsc/outF.wav", 'rb')
wm = wave.open("rsc/outM.wav", 'rb')

fr = wf.getframerate()
p = pyaudio.PyAudio()

print(wf.getsampwidth())
data = []
d = wf.readframes(CHUNK)
while len(d) > 0:
    data += [d]
    d = wf.readframes(CHUNK)

start = 0
end = len(data)-1

d = wm.readframes(CHUNK)
while len(d) > 0:
    data += [d]
    d = wm.readframes(CHUNK)

    
def callback(in_data, frame_count, time_info, status):
    clip = random.randint(start,end)
    print("playing clip {}".format(clip))
    return (data[clip], pyaudio.paContinue)

streams = []
for i in range(10):
    streams += [p.open(format=p.get_format_from_width(wf.getsampwidth()),
                       channels=wf.getnchannels(),
                       rate=wf.getframerate(),
                       output=True,
                       start=False,
                       frames_per_buffer=wf.getframerate(),
                       stream_callback=callback)]


for stream in streams:
    stream.start_stream()
    time.sleep(0.1)

    
time.sleep(5)
start = 0#end+1
end = len(data)-1
while True:
    pass

p.terminate()
