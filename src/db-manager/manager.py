import pandas as pd

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    def __init__(self, database_url:str, Base:any):
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

        Base.metadata.create_all(bind=self.engine)

    def _get_session(self):
        return self.SessionLocal()
    
    def insert_data(self, model_instance):
        session = self._get_session()
        with session.begin():
            session.add(model_instance)
        session.close()

    def bulk_insert_dataframe(self, df: pd.DataFrame, model_cls):
        """
        Insere DataFrame rapidamente via bulk_insert.
        """
        records = df.to_dict(orient="records")
        with self.get_session() as session:
            session.bulk_insert_mappings(model_cls, records)
            session.commit()
    
    def to_sql_dataframe(self, df: pd.DataFrame, table_name: str, if_exists="append"):
        """
        Usa pandas.to_sql() para inserir o DataFrame inteiro.
        - if_exists = "append" | "replace" | "fail"
        """
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)

    def select_all(self, model) -> list[dict]:
        with self._get_session() as session:
            rows = session.execute(select(model)).scalars().all()
            cols = [c.name for c in model.__table__.columns]
            for row in rows:
                print(" | ".join(f"{c}: {getattr(row, c)}" for c in cols))

            return [{c: getattr(r, c) for c in cols} for r in rows]
