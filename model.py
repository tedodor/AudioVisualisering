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
                yield p.clips
    


if __name__=='__main__':

    import pyaudio

    p = pyaudio.PyAudio()
    m = []

    #Alice
    try:
        for i in range(1, 2):
            path = "/Volumes/A14SAMGR/TaltekDT2112/Moby/"
            points = extractor.extract_features(path + "c{}.wav".format(i),
                                                path + "analysis/c{}.f0".format(i))
            m+=points
    except:
        pass

    pickle.dump(m, open("/Volumes/A14SAMGR/TaltekDT2112/out2.pickle", "wb"))
    # for i in range(1,4):
    #     path = "/Volumes/A14SAMGR/TaltekDT2112/Crusoe/"
    #     points = extractor.extract_features(path + "crusoe0{}.wav".format(i),
    #                                         path + "Analys/crusoe0{}.f0".format(i))
    #     m.add_points(points)

    
    # m.start()
    # m.v.w.mainloop()
    
