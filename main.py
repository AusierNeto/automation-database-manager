import os

from dotenv import load_dotenv

from db_manager import DatabaseManager
from models import User, base
from constants import *


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if __name__ == "__main__":
    db = DatabaseManager(database_url=DATABASE_URL, base=base)
    # db.insert_data(User(name='Dimas', age=30))

    results = db.select_all(User)
    for user in results: 
        print(f"User: {user.name}, Age: {user.age}")
