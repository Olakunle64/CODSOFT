#!/usr/bin/python3
"""This module contains a class named <ContactBook> which is use
    to store individual contact details.
    """
import datetime
import models


class ContactBook():
    """This class contains a both instance attribute and
        methods

        instance attribute:
            name, phone number, email and address.

        Note: phone number must be unique for all contacts
    """
    def __init__(self, *args, **kwargs):
        """initializing the instance variables"""
        """for key, value in kwargs.items():
            print(key, value)"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.name = ""
            self.phone_number = ""
            self.email = ""
            self.address = ""
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string implementation of an instance"""
        return ("[{}]----{}".format(self.phone_number, self.__dict__))

    def to_dict(self):
        """return the dictionary attribute of an instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = datetime.datetime.isoformat(
                obj_dict["created_at"])
        obj_dict["updated_at"] = datetime.datetime.isoformat(
                obj_dict["updated_at"])
        return obj_dict

    def save(self):
        """save an instance to the json file"""
        key = self.phone_number
        isExist = models.storage._FileStorage__contacts.get(key)
        if isExist:
            print("Phone number already exists!")
            return False
        if key and not isExist:
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            models.storage.save()
            return True
