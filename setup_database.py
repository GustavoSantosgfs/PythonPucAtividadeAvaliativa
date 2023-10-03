import sqlite3

DATABASE = 'database.db'

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create the products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        code INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    print("Database setup completed!")

if __name__ == '__main__':
    setup_database()
