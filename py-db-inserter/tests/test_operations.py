import unittest
from db_inserter.operations import DatabaseOperations
from db_inserter.exceptions import InsertError, UpdateError

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        self.db_operations = DatabaseOperations()

    def test_insert(self):
        # Test successful insertion
        result = self.db_operations.insert("test_table", {"column1": "value1"})
        self.assertTrue(result)

        # Test insertion with invalid data
        with self.assertRaises(InsertError):
            self.db_operations.insert("test_table", {"column1": None})

    def test_update(self):
        # Test successful update
        result = self.db_operations.update("test_table", {"column1": "new_value"}, {"column1": "value1"})
        self.assertTrue(result)

        # Test update with invalid conditions
        with self.assertRaises(UpdateError):
            self.db_operations.update("test_table", {"column1": "new_value"}, {"column1": None})

    def test_delete(self):
        # Test successful deletion
        result = self.db_operations.delete("test_table", {"column1": "value1"})
        self.assertTrue(result)

        # Test deletion with invalid conditions
        result = self.db_operations.delete("test_table", {"column1": None})
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()