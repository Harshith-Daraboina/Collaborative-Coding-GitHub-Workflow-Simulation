# Student Management System

A simple CLI-based Student Management System written in Python.

## Features
- Add student
- View records
- Search / delete

## Work Distribution

| Person | Function (operations.py) | Test (tests/) | Responsibility |
| :--- | :--- | :--- | :--- |
| **Yuvansh** | `add_student(student)` | `test_add.py` | Add new student, handle input safely |
| **Arun** | `view_students()` | `test_view.py` | Return/display all students, handle empty list |
| **Om sai chand** | `search_student(student_id)` | `test_search.py` | Find student by ID, return correct results |
| **Mihir** | `delete_student(student_id)` | `test_delete.py` | Remove student from database, ensure deletion |

## Project Structure
```
student_management/
│
├── main.py
├── student.py
├── database.py
├── operations.py
├── cli.py
│
├── tests/
│   ├── test_add.py
│   ├── test_view.py
│   ├── test_search.py
│   ├── test_delete.py
│
├── students.json
├── README.md
├── CONTRIBUTING.md
└── Experience_Report.md
```
