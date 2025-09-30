from db_inserter.connection import DatabaseConnection
from db_inserter.operations import DatabaseOperations
from db_inserter.history import HistoryManager
from db_inserter.keys import KeyManager
from db_inserter.config import Config

def main():
    # Load configuration
    config = Config()
    db_config = config.load_from_file('config.json')

    # Establish database connection
    db_connection = DatabaseConnection(**db_config)
    db_connection.connect()

    # Initialize operations and history manager
    db_operations = DatabaseOperations(db_connection)
    history_manager = HistoryManager()

    # Example data to insert
    data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    # Insert data into the database
    try:
        db_operations.insert('users', data)
        history_manager.log_insert(data)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Update data example
    updated_data = {
        'email': 'john.newemail@example.com'
    }
    try:
        db_operations.update('users', updated_data, where={'name': 'John Doe'})
        history_manager.log_update(updated_data)
        print("Data updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Disconnect from the database
    db_connection.disconnect()

if __name__ == "__main__":
    main()