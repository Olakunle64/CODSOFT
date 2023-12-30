#!/usr/bin/python3
"""This module contains a class named <FileStorage>
    which serves as a storage engine for the class <ToDoList>
    """

import json
import os
from models.toDoList import ToDoList


class FileStorage():
    """A class for storing all ToDoLists instances.
        It has two class field attribute and 4 methods

        Class attribute:
            __file_path - the path to the file for storage
            __to_do_lists - a dictionary containing all to do lists

        Instance method:
            all: return the dictionary containing all to do lists
            new: store the new instance into the __to_do_list dictionary
            save: save the __to_do_list to a json file
            reload: load the json file back to the __to_do_list dictionary
    """
    __file_path = "file.json"
    __to_do_lists = {}

    def __init__(self):
        """initilaization constructor"""
        pass

    def all(self) -> dict:
        """return all to do lists as a dictionary"""
        return FileStorage.__to_do_lists

    def new(self, obj):
        """store an instance to the __to_do_list dict"""
        key = obj.id
        self.__to_do_lists[key] = obj

    def save(self):
        """safe the __to_do_lists dictionary to a json file"""
        with open(self.__file_path, "w") as f:
            real_obj = {}
            for key, value in self.__to_do_lists.items():
                real_obj[key] = value.to_dict()
            json.dump(real_obj, f)

    def reload(self):
        """load the json file back to the __to_do_list dictionary"""
        try:
            with open(self.__file_path, "r") as f:
                if os.path.getsize(self.__file_path) != 0:
                    all_obj = json.load(f)
                    for key, value in all_obj.items():
                        self.__to_do_lists[key] = ToDoList(**value)
        except FileNotFoundError:
            pass
