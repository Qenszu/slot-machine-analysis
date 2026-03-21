from player import Player

class Players:
    def __init__(self):
        self.dict = {}
        self.id_count = 0

    def add_player(self, nick="", balance=0):
        self.dict[self.id_count] = Player(self.id_count, nick, balance)
        self.id_count += 1
    
    def get_player(self, id):
        return self.dict[id]
    
    def number_of_active_players(self):
        counter = 0 
        for player in self.dict.values():
            if player.is_active:
                counter += 1
        
        return counter
    
    def players_info(self):
        for player in self.dict.values():
            player.info()
            print()
    
