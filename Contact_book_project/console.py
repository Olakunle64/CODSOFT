#!/usr/bin/python3
"""This module contains a console which will interact with
    the ContactBook class to perform several operations like:

    Display contact, add contact, delete contact, update contact
    and search contact.
    """

import cmd
from models.Contact_Book import ContactBook
from models import storage
import re


class contactConsole(cmd.Cmd):
    """A console for the ContactBook class"""

    prompt = "Phone-->$ "

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

    def do_add(self, line):
        """add new contact
            Here is the the guide on how to use this method:
                add <phone_number> <name>"""
        details = line.split()
        if len(details) < 1:
            print("***phone-number is missing***")
            return
        if len(details) < 2:
            print("***name is missing***")
            return
        obj = ContactBook()
        obj.phone_number = details[0]
        obj.name = details[1]
        isExists = obj.save()
        if isExists:
            print("{} created!".format(obj.phone_number))

    def do_display(self, line):
        """display the list of all contacts
            To use this method just type <display>
        """
        for contact in storage.all().values():
            print(str(contact))

    def do_search(self, line):
        """search for a particular contact details through phone
            number or name of the contact.

            Here is the guide on how to use this method:
            search <name> OR search <phone_number>
        """
        for contact in storage.all().values():
            if (line.split()[0] in contact.name or
                    line.split()[0] in contact.phone_number):
                print(str(contact))

    def do_update(self, line):
        """update any attribute in the contact details

            Here is the guide to use this method:
            update <phone_number> <attrINdictFORM>
        """
        if not line:
            print("*** phone_number is missing ***")
            return
        arg_list = line.split('{')
        if len(arg_list) < 2:
            print("*** dict_attribute is missing ***")
            return
        details_to_update = '{' + arg_list[1].strip()
        print(details_to_update)
        arg_list[0] = arg_list[0].strip()
        if not storage.all().get(arg_list[0]):
            print("*** invalid phone_number ***")
            return
        obj = storage.all().get(arg_list[0])
        dict_regex = re.search(r'^{(.*)}$', details_to_update)
        if dict_regex:
            try:
                dict_attr = eval(details_to_update.strip("'\""))
                print(dict_attr)
                for key, value in dict_attr.items():
                    setattr(obj, key, value)
                storage.new(obj)
                storage.save()
            except Exception as e:
                print("*** let the attribute you want to update\
                        be in form of a dict ***")
                return
            for key, value in dict_attr.items():
                print(key, value)
                setattr(obj, key, value)
            storage.new(obj)
            storage.save()
        else:
            print("*** let the attribute you want to\
                    update be in form of a dict ***")

    def do_delete(self, line):
        """ delete a to do list """
        if not line:
            print("*** phone_number is missing ***")
            return
        phone_number = line.split()[0]
        all_dict = storage.all()
        if all_dict.get(phone_number):
            del storage._FileStorage__to_do_lists[phone_number]
            storage.save()
            storage.reload()
        else:
            print("*** invalid id ***")


if __name__ == "__main__":
    contactConsole().cmdloop()
