INSERT_QUERY = "INSERT INTO users (name, age) VALUES ('Alice', 30)"
SELECT_QUERY = "SELECT * FROM users"
CREATE_TABLE_IF_NOT_EXISTS = "CREATE TABLE IF NOT EXISTS users ( \
    id SERIAL PRIMARY KEY, \
    name VARCHAR(100), \
    age INTEGER)"

DATABASE_URL = "postgresql+psycopg2://ausier:ausier@localhost/test_db"
