from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


class DatabaseManager:
    def __init__(self, database_url:str, base:any):
        self.engine = create_engine(
            url=database_url,
            pool_pre_ping=True,
            pool_recycle=1800,
            future=True
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine, 
            autoflush=False, 
            autocommit=False, 
            future=True
        )

        base.metadata.create_all(bind=self.engine)

    def _get_session(self):
        return self.SessionLocal()
    
    def insert_data(self, model_instance):
        session = self._get_session()
        with session.begin():
            session.add(model_instance)
        session.close()

    def execute_query(self, query):
        with self.session.begin():
            result = self.session.execute(text(query))
        return result
