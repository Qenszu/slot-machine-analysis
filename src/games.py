from game import Game

class Games:
    def __init__(self):
        self.dict = {}
        self.id_count = 0

    def add_game(self, name, reels, num_reels, payouts):
        self.dict[self.id_count] = Game(name, reels, num_reels, payouts)
        self.id_count += 1
        
    def info(self):
        print("---- ALL GAMES INFO ----")
        for i, game in enumerate(self.dict.values()):
            print(f"{i+1}: {game.name}")

    def get_game(self, id):
        return self.dict[id]