class DatabaseOperations:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, table, data):
        # Logic for inserting data into the specified table
        query = f"INSERT INTO {table} ({', '.join(data.keys())}) VALUES ({', '.join(['%s'] * len(data))})"
        self.execute_query(query, tuple(data.values()))

    def update(self, table, data, condition):
        # Logic for updating data in the specified table
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute_query(query, tuple(data.values()))

    def delete(self, table, condition):
        # Logic for deleting data from the specified table
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)

    def execute_query(self, query, params=None):
        # Logic for executing a raw SQL query
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()