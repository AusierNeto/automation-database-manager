from sqlalchemy import create_engine, select
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

    def select_all(self, model) -> list[dict]:
        with self._get_session() as session:
            rows = session.execute(select(model)).scalars().all()
            cols = [c.name for c in model.__table__.columns]
            for row in rows:
                print(" | ".join(f"{c}: {getattr(row, c)}" for c in cols))

            return [{c: getattr(r, c) for c in cols} for r in rows]

    def execute_query(self, query):
        with self.session.begin():
            result = self.session.execute(text(query))
        return result
