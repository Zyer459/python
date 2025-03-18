import sqlite3

from encryption import decrypt_note

def init_db():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name varchar(255) NOT NULL,
			password varchar(255) NOT NULL,
			salt BLOB NOT NULL
		);
	''')
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS notes (
			notes_id INTEGER PRIMARY KEY AUTOINCREMENT,
			user_id INTEGER NOT NULL,
			iv BLOB NOT NULL,
			note BLOB NOT NULL,
			tag BLOB NOT NULL,
			FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
		);
	''')
	conn.commit()
	conn.close()

def add_user(name, password, salt):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		INSERT INTO users
		(name, password, salt)
		VALUES (?, ?, ?);''',(name, password, salt)
	)
	conn.commit()
	conn.close()
	
def find_user(name):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT id, name FROM users WHERE name = ?;
	''', (name,))
	result = cursor.fetchone()
	conn.close()
	
	if result is not None and result[0] >= 0:
		return int(result[0])
	print('user not found')
	return None

def verify_password(name, password):
	userid = find_user(name)
	if userid is None:
		return
	
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT password, salt FROM users WHERE id = ?
	''', (userid,))
	result = cursor.fetchone()
	conn.close()
	
	if result[0] == password:
		return result[1]
	else:
		print('wrong password')
		return None
	
def del_user(name, password):
	userid = find_user(name)
	x = verify_password(name, password)
	if userid is None or x is False:
		return
	
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()

	cursor.execute('''
		DELETE FROM users WHERE name = ? AND password = ?
	''', (name, password)) # use on delete cascade in notes foreign key so deleting this also delete all notes with the same foreign key
	conn.commit()
	conn.close()
	

def add_note(user_id, iv, note, tag):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		INSERT INTO notes
		(user_id, iv, note, tag)
		VALUES (?, ?, ?, ?);
	''', (user_id, iv, note, tag))
	conn.commit()
	conn.close()
	
def retrive_notes(user_id, key):
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	cursor.execute('''
		SELECT iv, note, tag FROM notes WHERE user_id = ?;
	''', (user_id,))
	rows = cursor.fetchall()
	conn.close()
	decrypted_notes = []
	for row in rows:
		iv, cipher, tag = row
		decrypted_notes.append(decrypt_note(iv, cipher, tag, key))
	return decrypted_notes


#init_db() run python database.py to initialize db first