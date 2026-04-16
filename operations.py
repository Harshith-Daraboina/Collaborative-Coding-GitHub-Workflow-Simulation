# operations.py
# CRUD operations for Student Management System

from database import load_data, save_data
from student import Student

# 👤 Yuvansh — Add Student
# Responsibility: Add new student to database, Ensure no crash on input
def add_student(student):
    """
    To be implemented by Yuvansh.
    Test: tests/test_add.py
    """
    if not isinstance(student, Student):
        raise ValueError("Input must be a Student object")
    
    data = load_data()
    data.append(student.to_dict())
    save_data(data)

# 👤 Arun — View Students
# Responsibility: Return/display all students, Handle empty list properly
def view_students():
    """
    To be implemented by Arun.
    Test: tests/test_view.py
    """
    pass

# 👤 Om sai chand — Search Student
# Responsibility: Find student by ID, Return correct result
# 👤 Om sai chand — Search Student
# Responsibility: Find student by ID, Return correct result
def search_student(student_id):
    """
    Implemented by Om sai chand.
    Finds a student by their ID.
    """
    students = database.load_data()
    for student in students:
        if student.get('student_id') == student_id:
            return student
    return None

# 👤 Mihir — Delete Student
# Responsibility: Remove student from database, Ensure student is actually deleted
def delete_student(student_id):
    """Delete a student by ID and persist the change.

    Author: Mihir

    Args:
        student_id (str | int): Unique ID of the student to delete.

    Returns:
        bool: True if a student was deleted, False if no match was found.
    """
    students = load_data()
    original_count = len(students)

    # Compare IDs as strings so callers can pass either int or str safely.
    filtered_students = [
        student for student in students
        if str(student.get("student_id")) != str(student_id)
    ]

    if len(filtered_students) == original_count:
        return False

    save_data(filtered_students)
    return True
