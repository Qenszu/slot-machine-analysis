class Player:
    def __init__(self, player_id, nick="", balance=0):
        self.player_id = player_id
        if not nick:
            self.nick = "newPlayer" + str(player_id)
        else:
            self.nick = nick
        self.balance = balance
        self.is_active = True

    def info(self):
        status = "active" if self.is_active else "not active" 

        print(f"Player id: {self.player_id} is {status}")
        print(f"Player {self.nick} current balance: {self.balance}")

    def current_balance(self):
        return self.balance
    
    def set_active(self, flag=True):
        self.is_active = flag
    






p1 = Player(1, "Qenszu", 100)
p2 = Player(2, "", 8)

p1.info()
print(p1.current_balance())

p2.info()
print(p2.current_balance())