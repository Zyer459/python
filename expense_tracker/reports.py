import sqlite3
import matplotlib.pyplot as plt

def plot_spending_by_category():
	conn = sqlite3.connect("expense_tracker.db")
	cursor = conn.cursor()
	cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
	data = cursor.fetchall()
	conn.close
	
	if not data:
		print('no data available for visualization')
		return
	
	categories = [row[0] for row in data]
	amounts = [row[1] for row in data]
	
	plt.figure(figsize=(7,7))
	plt.pie(amounts, labels = categories, startangle = 90)
	plt.title('Spending by category')
	plt.show()
	
def plot_spending_trend():
	conn = sqlite3.connect('expense_tracker.db')
	cursor = conn.cursor()
	cursor.execute('SELECT date, SUM(amount) FROM expenses GROUP BY date ORDER BY date')
	data = cursor.fetchall()
	conn.close()
	
	if not data:
		print('no data for visualization')
		return
	
	dates = [row[0] for row in data]
	amounts = [row[1] for row in data]
	
	plt.figure(figsize = (10,5))
	plt.bar(dates, amounts, color="#4c72b0", width = 0.5)
	plt.xlabel('Date')
	plt.ylabel('Total spent (tk)')
	plt.xticks(rotation=45)
	plt.title('Spending trend over time')
	plt.grid(axis="y", linestyle="--", alpha=0.7)
	plt.show()
	

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
