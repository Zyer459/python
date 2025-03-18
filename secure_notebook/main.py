from database import *
from encryption import *

def menu():
	while True:
		print('1. Login')
		print('2. Register')
		print('3. Exit')
		login = False
		option1 = int(input('choose option: '))
		
		if option1 == 1:
			#list_ = [input('Enter username and password: ').split()]
			name, password = input('Enter username and password: ').split()
			
			if find_user(name) is not None:
				salt = verify_password(name, hash_password(password))
				#print(salt)
				if salt is not None:
					print(f'Welcome {name}')
					login = True
					
		elif option1 == 2:
			name, password = input('Enter username and password: ').split()
			add_user(name, hash_password(password), os.urandom(16))#salt
		
		elif option1 == 3:
			break
		
		while login == True:
			print('1. Add note')
			print('2. Delete note')
			print('3. View notes')
			print('4. Delete user and notes')
			print('5. Logout')
			option2 = int(input('choose option: '))
			
			if option2 == 1:
				print('enter note: ')
				note = str(input())
				
				key = generate_key_from_password(password, salt) #gen key
				iv, cipher, tag = encrypt_note(note, key) #encrypt note -> cipher
				
				
				add_note(find_user(name), iv, cipher, tag)
			elif option2 == 2:
				pass
			
			elif option2 == 3:
				all_notes = retrive_notes(find_user(name), generate_key_from_password(password, salt))
				
				print (all_notes)				
			
			elif option2 == 4:
				del_user(name, hash_password(password))
				break
			
			elif option2 == 5:
				login = False
				break

menu()
