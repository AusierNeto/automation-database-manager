# DatabaseManager

[![PyPI version](https://badge.fury.io/py/database-manager.svg)](https://pypi.org/project/database-manager/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**DatabaseManager** é uma classe utilitária para **gerenciamento simples de bancos de dados com SQLAlchemy**.  
O objetivo é fornecer uma interface rápida para **inserção de dados**, inclusive a partir de **pandas DataFrames**, além de consultas básicas, sem precisar escrever muito boilerplate.

---

## 🚀 Instalação

```bash
pip install database-manager
```

Dependências:
- [SQLAlchemy](https://www.sqlalchemy.org/) >= 2.0  
- [pandas](https://pandas.pydata.org/) >= 2.0  

---

## ⚡ Exemplo rápido

```python
import pandas as pd
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String
from database_manager import DatabaseManager

# Define base ORM
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)

# Cria DatabaseManager
db_url = "sqlite:///example.db"
db = DatabaseManager(db_url, Base)

# Inserção individual
new_user = User(name="Alice", age=30)
db.insert_data(new_user)

# Inserção em massa via DataFrame
df = pd.DataFrame([
    {"name": "Bob", "age": 25},
    {"name": "Carol", "age": 40},
])
db.bulk_insert_dataframe(df, User)

# Inserção direta com pandas.to_sql()
df2 = pd.DataFrame([
    {"id": 3, "name": "Daniel", "age": 35}
])
db.to_sql_dataframe(df2, "users", if_exists="append")

# Consulta
users = db.select_all(User)
print(users)
```

---

## 🛠️ Métodos principais

### `insert_data(model_instance)`
Insere uma instância ORM (ex.: `User`) no banco de dados.  
Retorna o objeto já persistido.

### `bulk_insert_dataframe(df: pd.DataFrame, model_cls)`
Converte um DataFrame em registros e faz **inserção em massa** via `bulk_insert_mappings`.  
Mais rápido que `insert_data` quando há muitos registros.

### `to_sql_dataframe(df: pd.DataFrame, table_name: str, if_exists="append")`
Usa `pandas.to_sql()` para inserir diretamente em uma tabela.  
Opções do `if_exists`: `"append"`, `"replace"`, `"fail"`.

### `select_all(model) -> list[dict]`
Executa `SELECT * FROM <tabela>` e retorna a lista de registros como dicionários.  
Também imprime os registros formatados.

---

## 📂 Estrutura mínima do projeto

```
src/
 └── database_manager/
      ├── __init__.py
      └── db_manager.py
```

---

## 📜 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
