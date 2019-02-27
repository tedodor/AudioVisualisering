import math, random, time
import audio, view

THRESH = 100

class Point:
    def __init__(self, x, y, clip):
        self.x = x
        self.y = y
        self.clip = clip

    def dist(self, x, y):
        return math.sqrt((x - self.x)**2 + (y - self.y)**2)

    
class Model:
    points = []
    def __init__(self, clips1, clips2):
        self.v = view.View(THRESH)
        self.fill(clips1, 0)
        self.fill(clips2, 250)
        self.draw()
        self.player = audio.Player(self.get_clips)
        
    def fill(self, clips, i):
        self.points += [Point(random.randint(0, 250)+i,random.randint(0, 500),c) for c in clips]

    def start(self):
        pass

    def draw(self):
        self.v.draw(self.points)
        
    def get_clips(self):
        x, y = self.v.get_mouse_pos()
        for p in self.points:
            if p.dist(x, y) < THRESH:
                yield p.clip
    


if __name__=='__main__':
    CHUNK = 8000
    import wave, pyaudio
    p = pyaudio.PyAudio()

    wf = wave.open("rsc/outF.wav", 'rb')
    fr = wf.getframerate()
    data1 = []
    d = wf.readframes(CHUNK)
    while len(d) > 0:
        data1 += [d]
        d = wf.readframes(CHUNK)


    wf = wave.open("rsc/outM.wav", 'rb')
    fr = wf.getframerate()
    data2 = []
    d = wf.readframes(CHUNK)
    while len(d) > 0:
        data2 += [d]
        d = wf.readframes(CHUNK)

    m = Model(data1, data2)

    m.v.w.mainloop()
