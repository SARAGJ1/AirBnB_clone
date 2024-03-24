#!/usr/bin/python3
"""This script is the base model"""

import datetime
import uuid


class BaseModel:
    """class that defines all common attributes/methods for other classes"""


    def __init__(self, my_number='', name=''):
        """define Public instance attributes"""

        self.my_number = my_number
        self.name = name
        self.updated_at = ''
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()

    def save(self):
        """Update the date of modification"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """create a dic"""

        self.updated_at = self.updated_at.isoformat()
        self.created_at = self.created_at.isoformat()
        obj_dict = {
                'my_number': self.my_number,
                'name': self.name,
                '__class__': type(self).__name__,
                'updated_at': self.updated_at,
                'id': str(self.id),
                'created_at': self.created_at
                }
        return obj_dict

    def __str__(self):
        """return the folowing format"""

        if self.updated_at = '':
            self.updated_at = self.created_at
        return ('[{}] ({}) {}'.
                format(type(self).__name__, str(self.id), self.__dict__))
