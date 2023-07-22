# AI_Startup_Suite/agents/Personal_Assistant/task_management.py

```python
class Task:
    def __init__(self, task_name, priority, due_date, recurring):
        self.task_name = task_name
        self.priority = priority
        self.due_date = due_date
        self.recurring = recurring

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, priority, due_date, recurring):
        task = Task(task_name, priority, due_date, recurring)
        self.tasks.append(task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.task_name != task_name]

    def get_tasks(self):
        return self.tasks

    def get_task_by_name(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                return task

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def get_tasks_by_due_date(self, due_date):
        return [task for task in self.tasks if task.due_date == due_date]

    def get_recurring_tasks(self):
        return [task for task in self.tasks if task.recurring]
```

This code defines a `Task` class and a `TaskManager` class for managing tasks in the Personal Assistant agent. The `Task` class represents a single task with properties such as task name, priority, due date, and recurring status. The `TaskManager` class provides methods for adding, removing, and retrieving tasks, as well as filtering tasks by priority, due date, and recurring status.