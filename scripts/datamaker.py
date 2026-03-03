import duckdb
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(current_dir, "data", "enterprise_local.db")

def setup():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    # Connect and create schema    
    with duckdb.connect(DB_PATH) as con:
        con.execute("DROP TABLE IF EXISTS sales")
        con.execute("""
            CREATE TABLE sales (
                id INTEGER,
                product TEXT,
                revenue INTEGER,
                region TEXT
            )
        """)
        # Populate with mock corporate data
        con.execute("""
            INSERT INTO sales VALUES 
            (1, 'GenAI Agent', 5000, 'North'),
            (2, 'Data Connector', 3000, 'South'),
            (3, 'GenAI Agent', 7500, 'East'),
            (4, 'Cloud Storage', 1200, 'West')
        """)
    print(f"Success! Database created at: {DB_PATH}")

if __name__ == "__main__":
    setup()