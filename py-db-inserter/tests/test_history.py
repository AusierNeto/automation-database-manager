import unittest
from db_inserter.history import HistoryManager

class TestHistoryManager(unittest.TestCase):

    def setUp(self):
        self.history_manager = HistoryManager()

    def test_log_insert(self):
        self.history_manager.log_insert("Test data")
        history = self.history_manager.get_history()
        self.assertIn("Inserted: Test data", history)

    def test_log_update(self):
        self.history_manager.log_update("Test data")
        history = self.history_manager.get_history()
        self.assertIn("Updated: Test data", history)

    def test_get_history(self):
        self.history_manager.log_insert("Test data 1")
        self.history_manager.log_update("Test data 2")
        history = self.history_manager.get_history()
        self.assertEqual(len(history), 2)

if __name__ == '__main__':
    unittest.main()