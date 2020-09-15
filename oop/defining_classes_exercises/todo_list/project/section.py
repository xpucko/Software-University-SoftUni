from typing import List

from oop.defining_classes_exercises.todo_list import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        tasks_list = list(filter(lambda x: x.name == task_name, self.tasks))
        if tasks_list:
            task = tasks_list[0]
            task.completed = True
            return f'Completed task {task.name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        completed_tasks_list = list(filter(lambda x: x.completed, self.tasks))
        [self.tasks.remove(t) for t in completed_tasks_list]
        return f'Cleared {len(completed_tasks_list)} tasks.'

    def view_section(self):
        result = f'Section {self.name}:\n'
        for t in self.tasks:
            result += t.details() + '\n'
        return result
