#!/usr/bin/python3
"""This module contains a class named <ToDoList> which is use
    to store a set of actions to be taken by a person.
    """
import datetime
import models
import uuid


class ToDoList():
    """This class contains a both instance attribute and
        methods

        instance attribute:
            titile, id, task, taskBreakdown, created_at, deadline
            and priority.

        instance method:
            __str__ : string implementation of an instace
            to_dict(): dictionary attribute of an instance
    """
    def __init__(self, *args, **kwargs):
        """initializing the instance variables"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    setattr(
                        self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.title = ""
            # self.priority = priority
            self.task = ""
            self.taskBreakdown = ""
            self.created_at = datetime.datetime.now()
            self.deadline = ""
            self.priority = 1
    """
    @property
    def deadline(self):
        \"\"\"a getter method for the deadline attribute\"\"\"
        return self.__deadline

    @deadline.setter
    def deadline(self, value):
        \"\"\"a setter method for the deadline attribute

            It ensures that correct format of deadline is given.
            Here is the correct format:
                dd/mm/yy/ hr:min:sec
        \"\"\"
        # dd/mm/yy/ hr:min:sec
        dy, mth, yr, hr, mint, secs = value.split('/: ')
        arg_list = [dy, mth, yr, hr, mint, secs]
        print(arg_list)
        if any(arg_list) == None:
            raise ValueError("*** invalid input for the deadline ***")
            self.__deadline = datetime.datetime(
            year=yr, month=mth, day=dy, hour=hr, minute=mint, second=secs)

    @property
    def priority(self):
        \"\"\" a getter for the priority attribute \"\"\"
        return self.__priority

    @priority.setter
    def priority(self, value):
        \"\"\" a setter method for the priority attribute.

            It ensures that the value of priority must
            between 1-5
        \"\"\"
        if value >= 1 and value <= 5:
            self.__priority = value
        else:
            raise ValueError("*** value must be between 1-5 ***")
    """

    def __str__(self):
        """string implementation of an instance"""
        return ("[{}]----{}".format(self.id, self.__dict__))

    def to_dict(self):
        """return the dictionary attribute of an instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = datetime.datetime.isoformat(
                obj_dict["created_at"])
        # obj_dict["deadline"] = datetime.datetime.isoformat(
        # obj_dict["deadline"])
        return obj_dict

    def save(self):
        """save an instance to the json file"""
        models.storage.new(self)
        models.storage.save()
