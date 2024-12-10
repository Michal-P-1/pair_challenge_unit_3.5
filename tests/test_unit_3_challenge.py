from lib.unit_3_challenge import find_todos

def test_function_returns_true():
    notes = ["note_1", "#TODO task_1", "note_2", "#TODO task_2"]
    todos = []
    for task in notes:
        if find_todos(task):
            todos.append(task)
    assert todos == ["#TODO task_1", "#TODO task_2"]

def test_function_returns_false():
    all_notes = ["note_1", "#TODO task_1", "note_2", "#TODO task_2"]
    notes = []
    for note in all_notes:
        if not find_todos(note):
            notes.append(note)
    assert notes == ["note_1", "note_2"]