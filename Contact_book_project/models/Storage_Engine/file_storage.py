#!/usr/bin/python3
"""This module contains a class named <FileStorage>
    which serves as a storage engine for the class <ContactBook>
    """

import json
import os
from models.Contact_Book import ContactBook


class FileStorage():
    """A class for storing all ContactBook instances.
        It has two class field attribute and 4 methods

        Class attribute:
            __file_path - the path to the file for storage
            __contacts - a dictionary containing all contacts

        Instance method:
            all: return the dictionary containing all contacts
            new: store the new instance into the __contacts dictionary
            save: save the __contacts to a json file
            reload: load the json file back to the __contacts dictionary
    """
    __file_path = "file.json"
    __contacts = {}

    def __init__(self):
        """initilaization constructor"""
        pass

    def all(self) -> dict:
        """return all contacts as a dictionary"""
        return FileStorage.__contacts

    def new(self, obj):
        """store an instance to the __contacts dict"""
        key = obj.phone_number
        self.__contacts[key] = obj

    def save(self):
        """safe the __contacts dictionary to a json file"""
        with open(self.__file_path, "w") as f:
            real_obj = {}
            for key, value in self.__contacts.items():
                real_obj[key] = value.to_dict()
            json.dump(real_obj, f)

    def reload(self):
        """load the json file back to the __contacts dictionary"""
        try:
            with open(self.__file_path, "r") as f:
                if os.path.getsize(self.__file_path) != 0:
                    all_obj = json.load(f)
                    for key, value in all_obj.items():
                        self.__contacts[key] = ContactBook(**value)
        except FileNotFoundError:
            pass
