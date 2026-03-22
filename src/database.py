import sqlite3
from datetime import datetime



class DatabaseManager:
    def __init__(self, path):
        self.path = path
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.path)
        print("Database is connected")
        
    def create_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS players (
                player_id INTEGER PRIMARY KEY, 
                nickname CHAR[20],
                join_date TEXT,
                is_active BOOL
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS games (
                game_id INTEGER PRIMARY KEY, 
                name TEXT,
                add_date TEXT,
                num_reels INTEGER
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS reels (
                game_id INTEGER, 
                symbol_name TEXT,
                probability FLOAT,
                payout FLOAT,
                FOREIGN KEY (game_id) REFERENCES games(game_id)
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS spins (
                spin_id INTEGER PRIMARY KEY, 
                player_id INTEGER,              
                game_id INTEGER,
                date TEXT,
                bet FLOAT,
                win FLOAT,
                FOREIGN KEY (player_id) REFERENCES players(player_id),
                FOREIGN KEY (game_id) REFERENCES games(game_id)
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS spin_reels (
                spin_id INTEGER,
                reels_id INTEGER, 
                result TEXT,
                FOREIGN KEY (spin_id) REFERENCES spins(spin_id)
            )
        """)
        self.conn.commit()

    def add_player(self, player):
        cursor = self.conn.execute("""
            INSERT INTO players (nickname, join_date, is_active) 
            VALUES (?, ?, ?)
        """, (player.nick, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), True))
        self.conn.commit()

        return cursor.lastrowid
    
    def add_game(self, game):
        cursor = self.conn.execute("""
            INSERT INTO games (name, add_date, num_reels) 
            VALUES (?, ?, ?)
        """, (game.name, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), game.num_reels))

        last_id = cursor.lastrowid

        for symbol, probability in game.reels.items():
            self.conn.execute("""
                INSERT INTO reels (game_id, symbol_name, probability, payout)
                VALUES (?, ?, ?, ?)
            """, (last_id, symbol, probability, game.payouts[symbol]))
        
        self.conn.commit()
        return last_id
    
    def add_spin(self, player, game, spin, bet):
        cursor = self.conn.execute("""
            INSERT INTO spins (player_id, game_id, date, bet, win)
            VALUES(?, ?, ?, ?, ?)
            """, (player.id, game.id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), bet, spin.result()))
        
        last_id = cursor.lastrowid
        
        for i, values in enumerate(spin.current_spin):
            self.conn.execute("""
                INSERT INTO spin_reels (spin_id, reels_id, result)
                VALUES (?, ?, ?)
            """, (last_id, i+1, values))
        
        self.conn.commit()




