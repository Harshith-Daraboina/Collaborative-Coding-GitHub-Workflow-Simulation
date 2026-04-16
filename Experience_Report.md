# Experience Report

## Roles And Contributions

This project followed a collaborative GitHub workflow where each contributor owned one function and its corresponding tests.

- Yuvansh: Planned ownership for add_student(student) and add-related tests.
- Arun: Planned ownership for view_students() and view-related tests.
- Om sai chand: Planned ownership for search_student(student_id) and search-related tests.
- Mihir: Implemented delete_student(student_id) in operations.py and completed test_delete.py with working unit tests.

### Mihir's Contributions

- Implemented delete_student(student_id) to remove a student by ID from persistent JSON data.
- Added clear function documentation and author attribution in operations.py.
- Completed tests/test_delete.py with unit tests for successful deletion of an existing student and verification that a deleted student cannot be found again.
- Used isolated test data setup so test execution does not affect main repository records.

## Challenges Faced

- Merge and coordination risk: Multiple contributors working in the same operations.py file can lead to merge conflicts when changes are made in nearby lines.
- Integration consistency: Different coding styles and assumptions (return values, ID types, import paths) can cause small integration bugs.
- Test execution differences: Running tests from different directories can produce import issues unless project paths are handled consistently.

## Insights On GitHub Workflows And Team Dynamics

- Branch-based development made parallel work safer by isolating each contributor's changes.
- Pull requests provide a useful checkpoint for review, discussion, and quality control before merging.
- Small, focused commits improve traceability and make reviews easier.
- Clear ownership reduced overlap and helped each contributor stay accountable for one functional area.

## Suggestions For Improvement

- Define a shared coding convention early (docstring style, return behavior, naming).
- Add a basic CI workflow to run tests automatically on every pull request.
- Standardize test execution commands in README for all environments.
- Use regular short sync updates to reduce duplicate work and prevent late merge conflicts.
