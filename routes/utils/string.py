import random
import string
import bcrypt

def generate_pass(length: str):
	password = []
	while len(password) != length:
		rand = random.randrange(2)
		if rand == 1:
			password.append(generate_int(10))
		else:
			password.append(generate_string(1))
	return (''.join(password))

def return_only_this(tofind: str, data: list):
	output = []
	for i in data:
		i['name'] = i['name'].lower()
		if i['name'].find(tofind.lower()) >= 0:
			output.append(i)
	return output

def generate_id(length: int):
	uid = []
	while len(uid) != length:
		rand = random.randrange(2)
		if rand == 1:
			uid.append(generate_int(10))
		else:
			uid.append(generate_string(1))
	return (''.join(uid))

def generate_int(length):
	return str(random.randrange(10))

def generate_string(length):
	letters = string.ascii_lowercase
	res = ''.join(random.choice(letters) for i in range(length))
	return res

def hash_pass(password):
	return bcrypt.hashpw(password, bcrypt.gensalt())

def check_pass(password, hash_pass):
	return bcrypt.checkpw(password, hash_pass)