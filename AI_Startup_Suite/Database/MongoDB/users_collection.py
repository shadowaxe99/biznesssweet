```python
import pymongo

class UsersCollection:
    def __init__(self, db):
        self.collection = db["users"]

    def create_user(self, user_data):
        return self.collection.insert_one(user_data)

    def get_user(self, user_id):
        return self.collection.find_one({"_id": user_id})

    def update_user(self, user_id, update_data):
        return self.collection.update_one({"_id": user_id}, {"$set": update_data})

    def delete_user(self, user_id):
        return self.collection.delete_one({"_id": user_id})
```
