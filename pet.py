import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        date TEXT,
        amount REAL,
        description TEXT,
        category TEXT
    )''')
    conn.commit()
    conn.close()

def add_expense(date, amount, description, category):
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("INSERT INTO expenses (date, amount, description, category) VALUES (?, ?, ?, ?)",
              (date, amount, description, category))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = c.fetchall()
    conn.close()
    return data
