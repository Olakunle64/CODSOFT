#!/usr/bin/python3
"""This module contains an instance of FileStorage class
    which is automatically called when this package is called
    """

from models.Storage_Engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
