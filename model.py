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
    def __init__(self, clips):
        self.v = view.View()
        self.fill(clips)
        self.draw()
        time.sleep(10)
        self.player = audio.Player(self.get_clips)

    def fill(self, clips):
        self.points = [Point(random.randint(0, 500),random.randint(0, 500),c) for c in clips]

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
    wf = wave.open("rsc/outF.wav", 'rb')
    fr = wf.getframerate()
    p = pyaudio.PyAudio()
    data = []
    d = wf.readframes(CHUNK)
    while len(d) > 0:
        data += [d]
        d = wf.readframes(CHUNK)

    m = Model(data)
    m.v.w.mainloop()
    while True:
        pass
