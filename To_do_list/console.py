#!/usr/bin/python3
"""This module contains a console which will interact with
    the ContactBook class to perform several operations like:

    Display contact, add contact, delete contact, update contact
    and search contact.
    """

import cmd
from models.toDoList import ToDoList
from models import storage
import re


class toDoListConsole(cmd.Cmd):
    """A console for the ContactBook class"""

    prompt = "toDoList-->$ "

    def do_quit(self, line):
        """a method to quit the console"""
        return True

    def do_EOF(self, line):
        """a method to quit the console when end of file is
        passed
        """
        print()
        return True

    def emptyline(self):
        """do not nothing when the user press just enter"""
        pass

    def do_create(self, line):
        """create new to do list
            Here is the the guide on how to use this method:
                create <title> <priority>"""
        details = line.split()
        if len(details) < 1:
            print("***title is missing***")
            return
        if len(details) < 2:
            print("***priority is missing***")
            return
        if not (details[1].isdigit() or
                (eval(details[1]) < 1 or eval(details[1]) > 5)):
            print("*** priority must be between 1-5 ***")
            return
        obj = ToDoList()
        obj.title = details[0]
        obj.priority = eval(details[1])
        obj.save()
        print("{} created!".format(obj.id))

    def do_display(self, line):
        """display the list of all to do lists
            To use this method just type <display>
        """
        for toDo in storage.all().values():
            print(str(toDo))

    def do_search(self, line):
        """search for a particular to do list through the id.

            Here is the guide on how to use this method:
            search <id>
        """
        for toDo in storage.all().values():
            if toDo.id == line.split()[0]:
                print(str(toDo))

    def do_priority(self, line):
        """search based on priority

            Here is the guide on how to use it:
                priority <value>
        """
        if not line:
            print("*** priority value is missing ***")
            return
        if not line.isdigit():
            print("*** priority value must be an integer ***")
            return
        priority = int(line)
        if priority < 1 or priority > 5:
            print("*** priority value must be between 1 or 5 ***")
            return
        for obj in storage.all().values():
            if obj.priority == priority:
                print(obj)

    def do_update(self, line):
        """update any attribute in the to do lists

            Here is the guide to use this method:
            update <obj_id> <attrINdictFORM>

            Here is how you specify the deadline attribute
            of the dictionary attribute you want to pass in.

            deadline: dd/mm/yy/ hr:min:sec
        """
        if not line:
            print("*** id is missing ***")
            return
        arg_list = line.split('{')
        if len(arg_list) < 2:
            print("*** dict_attribute is missing ***")
            return
        details_to_update = '{' + arg_list[1].strip()
        arg_list[0] = arg_list[0].strip()
        if not storage.all().get(arg_list[0]):
            print("*** invalid id ***")
            return
        obj = storage.all().get(arg_list[0])
        dict_regex = re.search(r'^{(.*)}$', details_to_update)
        if dict_regex:
            try:
                dict_attr = eval(details_to_update.strip("'\""))
                if not dict_attr.get("deadline"):
                    print("*** You must specify the <deadline>\
                            for the task ***")
                    return
                for key, value in dict_attr.items():
                    setattr(obj, key, value)
                storage.new(obj)
                storage.save()
            except Exception as e:
                print("*** let the attribute you want to\
                        update be in form of a dict ***")
                return
            for key, value in dict_attr.items():
                setattr(obj, key, value)
            storage.new(obj)
            storage.save()
        else:
            print("*** let the attribute you want to\
                    update be in form of a dict ***")

    def do_delete(self, line):
        """ delete a to do list """
        if not line:
            print("*** id is missing ***")
            return
        id_val = line.split()[0]
        all_dict = storage.all()
        if all_dict.get(id_val):
            del storage._FileStorage__to_do_lists[id_val]
            storage.save()
            storage.reload()
        else:
            print("*** invalid id ***")


if __name__ == "__main__":
    toDoListConsole().cmdloop()
