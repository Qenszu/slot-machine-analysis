class Game:
    def __init__(self, name, reels, num_reels, payouts):
        self.name = name
        self.reels = reels
        self.num_reels = num_reels
        self.payouts = payouts

    def info(self):
        print("---- GAME INFO ----")
        print(f"Game name: {self.name}")
        print(f"Number of reels: {self.num_reels}")
        print(f"Available symbols and probabilities:")
        self.display_reel()

    def display_reel(self):
        for i, (symbol, count) in enumerate(self.reels.items()):
            print(f"{i+1}. {symbol} ---> {count}%")

    def get_reels(self):
        return self.reels

    def display_payouts(self):
        for i, (symbol, count) in enumerate(self.payouts.items()):
            print(f"{i+1}. {symbol} --> {count}")
    
    def get_payouts(self):
        return self.payouts
    