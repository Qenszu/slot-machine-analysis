import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from datetime import datetime, timedelta

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


def quit_probability(ratio):
    if ratio <= 0:
        return 1
    elif 1 <= ratio <= 1.05:
        return 0.05
    elif ratio > 1.05:
        return min(1, ratio - 1)
    
    return (1 - ratio)/2






db = DatabaseManager("data/casino_sim.db")
db.connect()
db.create_tables()

players = Players(db)
start_balance = 1000

for i in range(1000):
    players.add_player(f"Player{i+1}", start_balance)

games = Games(db)
games.add_game("777", reels, 3, payouts)
#games.info()

g = games.get_game(1)
spin = Spin(g)

spins = 1000


for i in range(1000):
    p = players.get_player(i+1)
    print("Player: ", i+1)
    start_time = datetime.now()
    session_id = db.start_session(start_time.strftime("%Y-%m-%d %H:%M:%S"))
    for j in range(spins):
        spin_time = start_time + timedelta(seconds=j * random.uniform(3, 8))
        spin.start_spin()
        db.add_spin(p, g, spin, session_id, 10, spin_time.strftime("%Y-%m-%d %H:%M:%S"))
        p.update_balance(10, 10*spin.result())
        ratio = p.balance/start_balance
        if random.random() < quit_probability(ratio):
            break

    db.end_session(session_id, spin_time.strftime("%Y-%m-%d %H:%M:%S"))
    