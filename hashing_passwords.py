import argparse
import hashlib

#parsing
parser = argparse.ArgumentParser(description = 'hashing given password')
parser.add_argument('password', help = 'input password you want to hash')
parser.add_argument('-t', '--type', default = 'sha256', choices = ['sha256', 'sha512', 'md5'])
args = parser.parse_args()

#hashing
password = args.password
hashtype = args.type
m = getattr(hashlib,hashtype)()
m.update(password.encode()) #.encode() converts the 'password' into bytes because hash functions in Python require bytes, not strings
# m.update() processes the encoded password and adds it to the hash object.

#output
print(f'< hash-type: {hashtype} >')
print(m.hexdigest())
