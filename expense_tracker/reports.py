import sqlite3

def get_total_spent():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0

def get_spending_by_category():
    conn = sqlite3.connect("expense_tracker.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    categories = cursor.fetchall()
    conn.close()
    return categories
