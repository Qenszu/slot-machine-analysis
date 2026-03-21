import sqlite3


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
            CREATE TABLE IF NOT EXISTS spins (
                spin_id INTEGER PRIMARY KEY, 
                player_id INTEGER,
                FOREIGN KEY (player_id) REFERENCES players(player_id) 
                game_id INTEGER,
                date TEXT,
                bet FLOAT,
                win FLOAT
            )
        """)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS spin_reels (
                spin_id INTEGER,
                FOREIGN KEY (spin_id) REFERENCES spins(spin_id)
                reels_id INTEGER, 
                result TEXT
            )
        """)
        self.conn.commit()