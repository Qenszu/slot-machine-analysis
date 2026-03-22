import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from game import Game
from games import Games
from player import Player
from players import Players
from spin import Spin
from database import DatabaseManager

reels = {
    "lemon": 6,
    "cherry": 9,
    "clover": 14,
    "bell": 18,
    "diamond": 38,
    "chest": 12,
    "seven": 3
}

payouts = {
    "lemon": 42,
    "cherry": 36,
    "clover": 30,
    "bell": 22,
    "diamond": 11,
    "chest": 33,
    "seven": 70
}
"""
games = Games()
games.add_game("777", reels, 3, payouts)
game = games.get_game(0)
spin = Spin(game)
res = []
N = 1000
for j in range(N):
    player = Player(0, "CzarekBot", 1000)
    for i in range(1000):
        spin.start_spin()
        player.update_balance(1, spin.result())

    res.append(player.balance)

sume = sum(res)
mean = sume/N
maxi = max(res)
mini = min(res)
print(mean, maxi, mini)
"""


db = DatabaseManager("data/casino_sim.db")
db.connect()
db.create_tables()

players = Players(db)
players.add_player("Qenszu", 100)
players.add_player("Czarus", 1000)
players.add_player("Kamil", 500)

players.info()