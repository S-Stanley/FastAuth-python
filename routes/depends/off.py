from typing import Optional
from fastapi import Header, HTTPException, Request

import os
from dotenv import load_dotenv
load_dotenv('.env')

class off():
	def __init__(self, request: Request, token: Optional[str] = Header(None)):
		if token != os.getenv('TOKEN'):
			print('Wrong or empty token')
			raise HTTPException(status_code=404)
		return None