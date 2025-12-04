from .storage import TaskStorage

storage = TaskStorage()

def add_task(description: str, due_date: str = None):
    return storage.add_task(description, due_date)

def list_all_tasks():
    return storage.list_tasks()

def delete_task(task_id: int):
    storage.delete_task(task_id)
    return {"deleted": task_id}

def complete_task(task_id: int):
    return storage.complete_task(task_id)
