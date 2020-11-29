def check_already(all_users: list, uid: str):
	verif = True
	for usr in all_users:
		if usr.id == uid:
			verif = False
	return verif

def verif_params(params, checker):
	for item in checker:
		if item not in params:
			print(item)
			return False
	return True
