class Player:
    def __init__(self, nick, balance=0):
        self.id = None
        self.nick = nick
        self.balance = balance
        self.is_active = True

    def info(self):
        status = "active" if self.is_active else "not active" 

        print(f"Player id: {self.id} is {status}")
        print(f"Player {self.nick} current balance: {self.balance}")

    def current_balance(self):
        return self.balance
    
    def set_active(self, flag=True):
        self.is_active = flag

    def update_balance(self, cost, profit):
        self.balance += profit - cost

    def update_id(self, id):
        self.id = id