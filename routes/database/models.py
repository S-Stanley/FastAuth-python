from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .psql_config import Base


class UserModel(Base):
	__tablename__ = "users"

	id = Column(String, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	password = Column(String)