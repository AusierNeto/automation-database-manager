from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

from constants import *
from dotenv import load_dotenv

def get_engine():
    return create_engine(
        url=DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=1800,
        future=True
    )

def SessionLocal():
    engine = get_engine()
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    return Session()

def execute_query(session, query):
    with session.begin():
        result = session.execute(text(query))
    return result

if __name__ == "__main__":
    session = SessionLocal()
    
    print("Database session created successfully.")

    execute_query(session, CREATE_TABLE_IF_NOT_EXISTS)

    # execute_query(session, INSERT_QUERY)

    results = execute_query(session, SELECT_QUERY)
    for row in results:
        print(row)
