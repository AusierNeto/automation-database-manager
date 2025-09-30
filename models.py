from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

class User(base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)

