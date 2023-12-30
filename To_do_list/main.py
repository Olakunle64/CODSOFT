#!/usr/bin/python3

from models.toDoList import ToDoList
from models import storage

obj = ToDoList()
obj.title = "Alx project"
obj.priority = 1
#obj.deadline = "29/12/2023 4:39:30"
print(obj)
obj.save()
print(storage.all())
