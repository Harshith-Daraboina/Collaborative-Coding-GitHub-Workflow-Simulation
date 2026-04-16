# tests/test_add.py
# 👤 Yuvansh — Add Student Test

import unittest
import os
import json
from operations import add_student
from student import Student
from database import DB_FILE

class TestAddStudent(unittest.TestCase):
    def setUp(self):
        # Backup original data
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r') as f:
                self.backup = json.load(f)
        else:
            self.backup = []
        # Start with empty data for tests
        with open(DB_FILE, 'w') as f:
            json.dump([], f)

    def tearDown(self):
        # Restore original data
        with open(DB_FILE, 'w') as f:
            json.dump(self.backup, f)

    def test_add_student_success(self):
        # Test adding a valid student
        student = Student(1, "John Doe", 20, "Computer Science")
        add_student(student)
        
        # Check if student was added
        with open(DB_FILE, 'r') as f:
            data = json.load(f)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['student_id'], 1)
        self.assertEqual(data[0]['name'], "John Doe")
        self.assertEqual(data[0]['age'], 20)
        self.assertEqual(data[0]['course'], "Computer Science")

    def test_add_student_no_crash_on_bad_input(self):
        # Test that invalid input raises ValueError
        with self.assertRaises(ValueError):
            add_student("not a student")
        
        with self.assertRaises(ValueError):
            add_student(123)
        
        with self.assertRaises(ValueError):
            add_student(None)
