from game import Game

class Games:
    def __init__(self, db):
        self.dict = {}
        self.db = db

    def add_game(self, name, reels, num_reels, payouts):
        g = Game(name, reels, num_reels, payouts)
        id = self.db.add_game(g)
        g.update_id(id)
        self.dict[id] = g 
        
    def info(self):
        print("---- ALL GAMES INFO ----")
        for i, game in enumerate(self.dict.values()):
            print(f"{i+1}: {game.name}")

    def get_game(self, id):
        return self.dict[id]