import math, random, time, pickle
import player, view, extractor

THRESH = 25

class Model:
    points = []
    def __init__(self):
        self.threshold = THRESH
        self.v = view.View(self.threshold)
        self.points = []

    def add_points(self, points):
        self.points += points
        
    def start(self):
        self.draw()
        self.player = player.Player(self.get_clips)
        
    def draw(self):
        self.v.draw(self.points)
        
    def get_clips(self):
        x, y = self.v.get_mouse_pos()
        for p in self.points:
            if p.dist(x, y) < self.threshold and p.clips:
                yield p.clips[self.v.clip_type]
    


if __name__=='__main__':

    import pyaudio

    p = pyaudio.PyAudio()
    m = Model()

    for i in range(1, 137):
        #Alice
        path = "/Volumes/A14SAMGR/TaltekDT2112/Moby/"
        points = extractor.extract_features(path + "c{}.wav".format(i),
                                            path + "analysis/c{}.f0".format(i))
        m.add_points(points)    

    m.start()
    m.v.w.mainloop()
     
