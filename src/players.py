from player import Player
from database import DatabaseManager

class Players:
    def __init__(self, db):
        self.dict = {}
        self.db = db

    def add_player(self, nick, balance=0):
        #TODO: validate unique nickname
        p = Player(nick, balance)
        id = self.db.add_player(p)
        p.update_id(id)
        self.dict[id] = p
    
    def get_player(self, id):
        return self.dict[id]
    
    def number_of_active_players(self):
        counter = 0 
        for player in self.dict.values():
            if player.is_active:
                counter += 1
        
        return counter
    
    def info(self):
        for player in self.dict.values():
            player.info()
            print()
    
