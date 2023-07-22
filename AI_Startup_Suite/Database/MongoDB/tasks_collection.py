```python
from pymongo import MongoClient

class TasksCollection:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['AI_Startup_Suite']
        self.collection = self.db['tasks']

    def create_task(self, task):
        self.collection.insert_one(task)

    def get_task(self, task_id):
        return self.collection.find_one({'_id': task_id})

    def update_task(self, task_id, updated_task):
        self.collection.update_one({'_id': task_id}, {'$set': updated_task})

    def delete_task(self, task_id):
        self.collection.delete_one({'_id': task_id})

    def get_all_tasks(self):
        return self.collection.find()
```
