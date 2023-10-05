import sqlite3

DATABASE = 'database.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        code INTEGER PRIMARY KEY,
        description TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    print("Database setup completed!")

if __name__ == '__main__':
    setup_database()
