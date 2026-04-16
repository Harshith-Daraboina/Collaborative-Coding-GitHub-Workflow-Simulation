# tests/test_delete.py
# 👤 Mihir — Delete Student Test

import os
import sys
import tempfile
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import database
from operations import delete_student

class TestDeleteStudent(unittest.TestCase):
    """Unit tests for deleting student records.

    Author: Mihir
    """

    def setUp(self):
        self.original_db_file = database.DB_FILE
        self.temp_dir = tempfile.TemporaryDirectory()
        database.DB_FILE = os.path.join(self.temp_dir.name, "students_test.json")

        database.save_data([
            {"student_id": "101", "name": "Asha", "age": 20, "course": "CS"},
            {"student_id": "102", "name": "Ravi", "age": 21, "course": "Math"},
        ])

    def tearDown(self):
        database.DB_FILE = self.original_db_file
        self.temp_dir.cleanup()

    def test_delete_student_success(self):
        result = delete_student("101")

        self.assertTrue(result)
        remaining_students = database.load_data()
        self.assertEqual(len(remaining_students), 1)
        self.assertEqual(remaining_students[0]["student_id"], "102")

    def test_delete_student_actually_deleted(self):
        delete_student("101")
        remaining_students = database.load_data()

        self.assertFalse(any(s["student_id"] == "101" for s in remaining_students))
        self.assertFalse(delete_student("101"))

if __name__ == "__main__":
    unittest.main()
