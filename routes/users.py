from fastapi import FastAPI, HTTPException, APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from .services import users
from .utils.check import verif_params
from .utils.string import check_pass, generate_pass
from .depends.off import off

router = APIRouter()

@router.post('/users/inscription')
async def post(request: Request, self: off = Depends(off)):
	try:
		form = await request.form()
		if not verif_params(form, ['email', 'password']):
			return JSONResponse({'res': False, 'message': 'Incomplete form'})
		all_users = users.get_all_users()
		for usr in all_users:
			if usr.email == form['email']:
				return JSONResponse({'res': False, 'message':'This email address already exists'})
		if not users.create_user(form):
			return JSONResponse({'res': False, 'message': 'Error while creating your account, please try again later'})
		return JSONResponse({'res': True, 'message': "Registration validated, you can now connect"})
	except Exception as e:
		print(e)
		return JSONResponse({'res': False, 'message': 'Error, please try again later'})

@router.post('/users/connexion')
async def post(request: Request, self: off = Depends(off)):
	try:
		form = await request.form()
		if not verif_params(form, ['email', 'password']):
			return JSONResponse({'res': False, 'message': 'Incomplete form'})
		user = users.get_user_by_email(form['email'])
		if not user:
			return JSONResponse({'res': False, 'message': 'This email address is not linked to any account'})
		if check_pass(form['password'], user['password']):
			return JSONResponse({'res': True})
		else:
			return JSONResponse({'res': False, 'message': 'Incorrect password'})
	except Exception as e:
		print(e)
		return JSONResponse({'res': False, 'message': "Error, please try again later"})
