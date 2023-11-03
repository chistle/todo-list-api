from .firebase_config import db
from firebase_admin import firestore

class Task:
    collection = db.collection('tasks')

    def __init__(self, title, description, status='pending', id=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

    def create(self):
        doc_ref = self.collection.add(self.to_dict())
        self.id = doc_ref[1].id  
        return self.to_dict()

    @classmethod
    def get_all(cls):
        tasks_query = cls.collection.stream()
        tasks = []
        for task in tasks_query:
            task_dict = task.to_dict()
            task_dict['id'] = task.id
            tasks.append(task_dict)
        return tasks

    @classmethod
    def get_by_id(cls, task_id):
        task_ref = cls.collection.document(task_id)
        task = task_ref.get()
        if task.exists:
            return {**task.to_dict(), 'id': task.id}
        else:
            return None

    def update(self, task_id, update_data):
        task_ref = self.collection.document(task_id)
        task_ref.update(update_data)
        return {**update_data, 'id': task_id}

    @classmethod
    def delete(cls, task_id):
        task_ref = cls.collection.document(task_id)
        task_ref.delete()
        return True