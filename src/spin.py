import numpy as np
from game import Game

class Spin:
    def __init__(self, game):
        self.game = game
        self.current_spin = []
    

    def start_spin(self):
        reels = self.game.get_reels()
        num_reels = self.game.num_reels

        reels_probability = np.array(list(reels.values())) / 100

        self.current_spin = np.random.choice(list(reels.keys()), num_reels, p=reels_probability)
    
    def result(self):
        res = self.current_spin
        print(res)

        if len(res) == 0:
            return "Spin game first"

        if res[0] == res[1] == res[2]:
            return self.game.payouts[res[0]]
        
        return 0

