from sqlalchemy.orm import Session
from fastapi import Depends
import random

from ..database.models import UserModel
from ..database.psql_config import SessionLocal, engine

from ..database import models
from ..utils.string import generate_id, hash_pass
from ..utils.check import check_already

models.Base.metadata.create_all(bind=engine)


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

def get_all_users(db: Session = SessionLocal()):
	try:
		return (db.query(UserModel).all())
	except Exception as e:
		print(e)
		return False

def get_user_by_id(id: str, db: Session = SessionLocal()):
	try:
		usr = db.query(UserModel).filter_by(id=id).first()
		output = {}
		output['email'] = usr.email
		output['id'] = usr.id
		output['password'] = usr.password
		return output
	except Exception as e:
		print(e)
		return False

def get_user_by_email(email: str, db: Session = SessionLocal()):
	try:
		item = db.query(UserModel).filter_by(email=email).first()
		output = {}
		output['email'] = item.email
		output['id'] = item.id
		output['password'] = item.password
		return output
	except Exception as e:
		print(e)
		return False

def create_user(form, db: Session = SessionLocal()):
	try:
		uid = generate_id(23)
		all_users = get_all_users()
		while check_already(all_users, uid) == False:
			uid = generate_id(23)

		user = UserModel(id=uid, email=form['email'], password=hash_pass(form['password']))
		db.add(user)
		db.commit()
		db.refresh(user)
		return True
	except Exception as e:
		print(e)
		return False

def alter_user(form, db: Session = SessionLocal()):
	try:
		user = db.query(UserModel).filter_by(email=form['email']).first()
		if not user:
			return False
		user.name = form['name']
		db.add(user)
		db.commit()
		db.refresh(user)
		return True
	except Exception as e:
		print(e)
		return False

def alter_password(email:str, new_pass: str, db: Session = SessionLocal()):
	try:
		usr = db.query(UserModel).filter_by(email=email).first()
		if not usr:
			return False
		usr.password = hash_pass(new_pass)
		db.add(usr)
		db.commit()
		db.refresh(usr)
		return True
	except Exception as e:
		print(e)
		return False