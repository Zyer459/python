import sqlite3

def init_db():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date varchar(255),
            category varchr(255),
            amount REAL,
            description varchar(255)
        );
    ''')
    conn.commit()
    conn.close()

def add_expense(date, category, amount, description):
	conn =  sqlite3.connect('expense_tracker.db')
	cursor = conn.cursor()
	cursor.execute(
		'''INSERT INTO expenses
			(date, category, amount, description)
			VALUES (?, ?, ?, ?)''',(date, category, amount, description)
	)
	conn.commit()
	conn.close()

def get_expense():
	conn = sqlite3.connect('expense_tracker.db')
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM expenses ORDER BY date DESC')
	expenses = cursor.fetchall()
	conn.close()
	return expenses

if __name__ == "__main__":
    init_db()
