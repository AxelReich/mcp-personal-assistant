import json
import os
from threading import Lock

class TaskStorage:
    def __init__(self, filename="tasks.json"):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.lock = Lock()

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def list_tasks(self):
        with self.lock:
            return self._load()

    def add_task(self, description, due_date):
        with self.lock:
            data = self._load()
            new_id = data[-1]["id"] + 1 if data else 1

            task = {
                "id": new_id,
                "description": description,
                "due_date": due_date,
                "done": False
            }

            data.append(task)
            self._save(data)
            return task

    def delete_task(self, task_id):
        with self.lock:
            data = self._load()
            data = [t for t in data if t["id"] != task_id]
            self._save(data)

    def complete_task(self, task_id):
        with self.lock:
            data = self._load()
            for t in data:
                if t["id"] == task_id:
                    t["done"] = True
                    self._save(data)
                    return t
            raise ValueError("Task not found")
